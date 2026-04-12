from env.models import Observation, Action
from env.tasks import TASKS
import random

class EmailTriageEnv:
    """Email Triage RL Environment with task grading support."""
    
    # Class attributes for task discovery
    TASKS = TASKS
    GRADERS = {t["name"]: t["grader"] for t in TASKS if "grader" in t}
    
    def __init__(self):
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(TASKS)

        return {
            "observation": Observation(
                email_text=self.current_task["email"],
                sender="unknown",
                history=[]
            ),
            "reward": 0.5,
            "done": False,
            "info": {}
        }

    def step(self, action: Action):
        expected = self.current_task["expected"]
        task_name = self.current_task["name"]
        
        # Use grader if available
        if "grader" in self.current_task:
            reward = self.current_task["grader"](action, expected)
        else:
            # Fallback reward calculation
            reward = 0.3

            if action.label == expected["label"]:
                reward += 0.2
            else:
                reward -= 0.05

            if action.priority == expected["priority"]:
                reward += 0.2
            else:
                reward -= 0.05

            requires = expected.get("requires", [])
            reply_text = action.reply.lower()

            keyword_hits = sum(1 for kw in requires if kw in reply_text)

            if requires:
                ratio = keyword_hits / len(requires)
                reward += 0.2 * ratio

            if task_name == "easy_spam":
                reward += 0.05 if "spam" in reply_text else 0

            elif task_name == "medium_meeting":
                reward += 0.05 if "meeting" in reply_text else 0

            elif task_name in ["hard_multi", "support_request"]:
                reward += 0.05 if ("call" in reply_text or "help" in reply_text) else 0

            reward = max(0.05, min(0.95, reward))

        return {
            "observation": Observation(
                email_text=self.current_task["email"],
                sender="unknown",
                history=[]
            ),
            "reward": float(reward),
            "done": True,
            "info": {"task": task_name}
        }

    def state(self):
        return {"task": self.current_task}
    
    def get_tasks_with_graders(self):
        """Return list of tasks that have graders.
        
        Used by validators to discover graded tasks.
        """
        return [
            {
                "name": task["name"],
                "has_grader": "grader" in task,
                "grader_function": task.get("grader").__name__ if "grader" in task else None,
            }
            for task in TASKS
        ]