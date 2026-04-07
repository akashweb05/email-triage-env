from fastapi import FastAPI
import uvicorn

from env.environment import EmailTriageEnv
from env.models import Action
from env.tasks import TASKS

app = FastAPI()
env = EmailTriageEnv()

@app.get("/")
def home():
    return {"message": "Email Triage Env is running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    action_obj = Action(**action)
    return env.step(action_obj)

@app.get("/state")
def state():
    return env.state()

@app.get("/metadata")
def metadata():
    return {
        "name": "email_triage_env",
        "description": "RL environment for email triage",
        "tasks": [task["name"] for task in TASKS]
    }

@app.get("/schema")
def schema():
    return {
        "observation": {
            "email_text": "string",
            "sender": "string",
            "history": "list"
        },
        "action": {
            "label": "string",
            "priority": "integer",
            "reply": "string"
        }
    }

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
