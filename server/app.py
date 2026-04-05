from fastapi import FastAPI
import uvicorn

from env.environment import EmailTriageEnv
from env.models import Action

app = FastAPI()
env = EmailTriageEnv()

@app.get("/")
def home():
    return {"message": "Email Triage Env is running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    action_obj = Action(**action)
    return env.step(action_obj)

@app.get("/state")
def state():
    return env.state()

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()