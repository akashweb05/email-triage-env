from env.models import Observation, Action
from env.tasks import TASKS
import random

class EmailTriageEnv:

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
            "reward": 0.1,
            "done": False,
            "info": {}
        }

    def step(self, action: Action):
        expected = self.current_task["expected"]

        reward = 0.1

        if action.label == expected["label"]:
            reward += 0.3
        else:
            reward += 0.1

        if action.priority == expected["priority"]:
            reward += 0.3
        else:
            reward += 0.1

        keyword_hits = sum(
            1 for kw in expected.get("requires", [])
            if kw in action.reply.lower()
        )

        if expected.get("requires"):
            reward += 0.3 * (keyword_hits / len(expected["requires"]))

        reward = max(0.1, min(0.95, reward))

        return {
            "observation": Observation(
                email_text=self.current_task["email"],
                sender="unknown",
                history=[]
            ),
            "reward": float(reward),
            "done": True,
            "info": {"task": self.current_task["name"]}
        }

    def state(self):
        return {"task": self.current_task}
