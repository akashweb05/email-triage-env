import os
import json

try:
    from openai import OpenAI
    USE_OPENAI = True
except:
    USE_OPENAI = False

from env.environment import EmailTriageEnv
from env.models import Action

API_BASE_URL = os.environ.get("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.environ.get("HF_TOKEN")

# Initialize OpenAI client with provided credentials
client = None
if USE_OPENAI and HF_TOKEN:
    client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

env = EmailTriageEnv()

# MOCK AGENT (fallback)
def mock_agent(email_text):
    text = email_text.lower()

    if "free" in text or "win" in text:
        return Action(label="spam", priority=1, reply="This is spam.")

    elif "meeting" in text:
        return Action(label="important", priority=5, reply="I will attend the meeting.")

    else:
        return Action(
            label="important",
            priority=5,
            reply="Sorry for the issue. Let's schedule a call."
        )

# MAIN AGENT
def get_model_action(email_text):
    if client:
        try:
            prompt = f"""
            Classify this email:
            {email_text}

            Return ONLY JSON:
            {{
                "label": "spam/important/promo",
                "priority": 1-5,
                "reply": "your reply"
            }}
            """

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.choices[0].message.content.strip()
            data = json.loads(content)

            return Action(**data)

        except Exception:
            # fallback if API fails
            return mock_agent(email_text)

    else:
        return mock_agent(email_text)


def main():
    try:
        result = env.reset()
        
        print(f"[START] task=email_triage env=email-triage model={MODEL_NAME}", flush=True)
        
        rewards = []
        steps_taken = 0
        success = False
        score = 0.0
        
        # Run one step
        action = get_model_action(result["observation"].email_text)
        result = env.step(action)
        
        reward = float(result.get("reward", 0.0))
        done = result.get("done", True)
        
        steps_taken = 1
        rewards.append(reward)
        
        # Normalize score to [0, 1]
        score = min(max(reward, 0.0), 1.0)
        success = score > 0.0
        
        print(f"[STEP] step=1 action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)
        
        # Format rewards correctly
        rewards_str = ",".join(f"{r:.2f}" for r in rewards)
        print(f"[END] success={str(success).lower()} steps={steps_taken} score={score:.2f} rewards={rewards_str}", flush=True)
        
    except Exception as e:
        print(f"[END] success=false steps=0 score=0.00 rewards=", flush=True)
        raise


if __name__ == "__main__":
    main()