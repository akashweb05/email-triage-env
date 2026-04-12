from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from env.environment import EmailTriageEnv
from env.models import Action
from env.tasks import (
    TASKS,
    TASK_LIST,
    TASK_COUNT,
    TASKS_WITH_GRADERS,
    GRADER_SPECS,
    SINGLE_GRADER_SPECS,
)

app = FastAPI(
    title="Email Triage OpenEnv",
    version="1.0.0",
    description="OpenEnv-compliant email triage environment with 4 graded tasks"
)

# Enable CORS for validator
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

_envs: dict = {}

def _tasks_with_graders() -> int:
    """Count tasks that have graders"""
    return TASKS_WITH_GRADERS

def _grader_registry() -> dict:
    """Return detailed grader specifications by task"""
    return GRADER_SPECS

def _single_grader_registry() -> dict:
    """Return single grader spec per task"""
    return SINGLE_GRADER_SPECS

def _task_payloads() -> list:
    """Return task list with grader metadata for validator"""
    payloads = []
    for task in TASK_LIST:
        payload = {
            key: value
            for key, value in task.items()
            if key not in {"grader", "graders", "grader_spec"}
        }
        payload["grader_spec"] = task.get("grader_spec")
        payload["has_grader"] = callable(task.get("grader"))
        payloads.append(payload)
    return payloads

env = EmailTriageEnv()

@app.get("/")
def home():
    return {
        "name": "email_triage_env",
        "message": "Email Triage OpenEnv is running",
        "status": "ok",
        "tasks_with_graders": _tasks_with_graders(),
        "total_tasks": TASK_COUNT,
    }

@app.get("/health")
def health():
    return {"status": "ok", "tasks_with_graders": _tasks_with_graders()}

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
    """Return complete metadata including grader registry"""
    return {
        "name": "email_triage_env",
        "description": "RL environment for email triage with 4 graded tasks",
        "version": "1.0",
        "task_count": TASK_COUNT,
        "tasks_with_graders": _tasks_with_graders(),
        "grader_count": _tasks_with_graders(),
        "tasks": _task_payloads(),
        "graders": _grader_registry(),
        "grader_registry": _single_grader_registry(),
        "all_have_graders": _tasks_with_graders() == TASK_COUNT,
    }

@app.get("/tasks")
def list_tasks():
    """List all tasks with grader metadata"""
    return {
        "tasks": _task_payloads(),
        "count": TASK_COUNT,
        "task_count": TASK_COUNT,
        "tasks_with_graders": _tasks_with_graders(),
        "grader_count": _tasks_with_graders(),
        "all_have_graders": _tasks_with_graders() == TASK_COUNT,
        "graders": _grader_registry(),
        "grader_registry": _single_grader_registry(),
    }

@app.get("/grading-config")
def grading_config():
    """Return grading configuration for validator discovery"""
    return {
        "grading_enabled": True,
        "num_graded_tasks": _tasks_with_graders(),
        "graded_task_names": list(TASKS.keys()),
        "grader_specs": _grader_registry(),
        "single_grader_specs": _single_grader_registry(),
        "grader_registry": {
            task_id: {
                "name": task.get("grader_spec", {}).get("name", f"grade_{task_id}"),
                "task_id": task_id,
                "task_name": task.get("name", ""),
                "has_grader": callable(task.get("grader")),
                "entrypoint": task.get("grader_spec", {}).get("entrypoint", ""),
            }
            for task_id, task in TASKS.items()
        }
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

@app.get("/tasks-info")
def tasks_info():
    """Get list of all tasks with grader status for validator discovery."""
    return {
        "tasks": _task_payloads(),
        "tasks_with_graders": _tasks_with_graders(),
        "total_tasks": TASK_COUNT,
    }

@app.get("/tasks-with-graders")
def tasks_with_graders():
    """Return task list with grader availability (for validator)"""
    from env.models import Action
    
    tasks_info = []
    for task_id, task in TASKS.items():
        grader_info = {
            "name": task.get("name", task_id),
            "task_id": task_id,
            "has_grader": callable(task.get("grader")),
            "difficulty": task.get("difficulty", ""),
            "description": task.get("description", ""),
        }
        
        # If task has grader, test it
        if callable(task.get("grader")):
            try:
                test_action = Action(
                    label=task["expected"]["label"],
                    priority=task["expected"]["priority"],
                    reply=" ".join(task["expected"].get("requires", []))
                )
                score = task["grader"](test_action, task["expected"])
                grader_info["grader_available"] = True
                grader_info["test_score"] = float(score)
                grader_info["score_valid"] = 0 < score < 1
                grader_info["grader_name"] = task.get("grader_spec", {}).get("name", "")
            except Exception as e:
                grader_info["grader_available"] = False
                grader_info["error"] = str(e)
        else:
            grader_info["grader_available"] = False
        
        tasks_info.append(grader_info)
    
    return {
        "tasks_with_graders": tasks_info,
        "total_tasks_with_graders": _tasks_with_graders(),
        "total_tasks": TASK_COUNT,
        "all_have_graders": _tasks_with_graders() == TASK_COUNT,
    }

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
