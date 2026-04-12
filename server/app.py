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

@app.get("/tasks-with-graders")
def tasks_with_graders():
    """Return task list with grader availability (for validator)"""
    from env.models import Action
    
    tasks_info = []
    for task in TASKS:
        grader_info = {
            "name": task["name"],
            "has_grader": "grader" in task,
            "grader_callable": callable(task.get("grader")),
        }
        
        # Test grader if available
        if "grader" in task:
            try:
                test_action = Action(
                    label=task["expected"]["label"],
                    priority=task["expected"]["priority"],
                    reply=" ".join(task["expected"].get("requires", []))
                )
                test_score = task["grader"](test_action, task["expected"])
                grader_info["test_score"] = float(test_score)
                grader_info["score_valid"] = 0 < test_score < 1
            except Exception as e:
                grader_info["test_error"] = str(e)
        
        tasks_info.append(grader_info)
    
    return {
        "total_tasks": len(TASKS),
        "tasks_with_graders_count": len([t for t in TASKS if "grader" in t]),
        "tasks": tasks_info
    }

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
