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
            "reward": 0.0,
            "done": False,
            "info": {}
        }

    def step(self, action: Action):
        expected = self.current_task["expected"]

        reward = 0

        if action.label == expected["label"]:
            reward += 0.4

        if action.priority == expected["priority"]:
            reward += 0.3

        if "sorry" in action.reply.lower():
            reward += 0.15

        if "call" in action.reply.lower():
            reward += 0.15

        return {
            "observation": Observation(
                email_text=self.current_task["email"],
                sender="unknown",
                history=[]
            ),
            "reward": reward,
            "done": True,
            "info": {}
        }

    def state(self):
        return {"task": self.current_task}