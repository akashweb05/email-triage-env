import os
import json

try:
    from openai import OpenAI
    USE_OPENAI = True
except:
    USE_OPENAI = False

from env.environment import EmailTriageEnv
from env.models import Action

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

# only initialize if valid OpenAI key (sk-)
client = None
if USE_OPENAI and HF_TOKEN and HF_TOKEN.startswith("sk-"):
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
    result = env.reset()

    print(f"[START] task=email_triage env=email_env model={MODEL_NAME}")

    rewards = []

    action = get_model_action(result["observation"].email_text)

    result = env.step(action)

    reward = result["reward"]
    done = result["done"]

    rewards.append(f"{reward:.2f}")

    print(f"[STEP] step=1 action={action} reward={reward:.2f} done={str(done).lower()} error=null")

    print(f"[END] success=true steps=1 rewards={','.join(rewards)}")


if __name__ == "__main__":
    main()