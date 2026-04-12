from env.models import Observation, Action
from env.tasks import TASKS, TASK_LIST, TASKS_BY_ID, TASKS_WITH_GRADERS, TASK_NAMES_WITH_GRADERS
import random

class EmailTriageEnv:
    """Email Triage RL Environment with task grading support."""
    
    # Class attributes for task discovery (matches r-vb/bug-triage-env pattern)
    TASKS = TASKS  # List version for iteration
    TASKS_DICT = TASKS_BY_ID  # Dict version for lookup
    TASK_LIST = TASK_LIST
    GRADERS = {task_id: task["grader"] for task_id, task in TASKS_BY_ID.items() if callable(task.get("grader"))}
    
    # Explicit class-level metadata for validators
    GRADED_TASK_NAMES = TASK_NAMES_WITH_GRADERS
    NUM_GRADED_TASKS = TASKS_WITH_GRADERS
    TASK_COUNT = len(TASKS_BY_ID)
    
    def __init__(self):
        self.current_task = None
        self.task_id = None

    def reset(self):
        # Select a random task from TASK_LIST
        self.current_task = random.choice(TASK_LIST)
        self.task_id = self.current_task.get("id") or self.current_task.get("name")

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
        task_name = self.current_task.get("name") or self.current_task.get("id", "")
        
        # Use grader if available
        if callable(self.current_task.get("grader")):
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

            if "spam" in task_name or "easy" in task_name:
                reward += 0.05 if "spam" in reply_text else 0

            elif "meeting" in task_name or "medium" in task_name:
                reward += 0.05 if "meeting" in reply_text else 0

            elif "multi" in task_name or "support" in task_name or "hard" in task_name:
                reward += 0.05 if ("call" in reply_text or "help" in reply_text) else 0

            reward = max(0.005, min(0.994, reward))

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