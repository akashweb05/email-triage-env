# 📧 Email Triage OpenEnv Environment

## 🚀 Overview

This project implements a **real-world reinforcement learning environment** for **email triage**, built using the OpenEnv framework.

The environment simulates how humans process emails by:

* Classifying emails (spam / important / promo)
* Assigning priority levels
* Generating appropriate replies

It is designed to **train and evaluate AI agents** on practical workplace tasks such as inbox management.

---

## 🎯 Motivation

Email overload is a real problem in modern workflows. Automating email triage can:

* Improve productivity
* Reduce response delays
* Assist customer support teams

This environment provides a **standardized benchmark** for evaluating such AI systems.

---

## 🧠 Environment Design

### 🔹 Observation Space

```json
{
  "email_text": "string",
  "sender": "string",
  "history": ["previous actions"]
}
```

---

### 🔹 Action Space

```json
{
  "label": "spam | important | promo",
  "priority": "1-5",
  "reply": "string"
}
```

---

### 🔹 Reward Function

The reward function provides **dense feedback**:

* ✅ Correct classification → +0.4
* ✅ Correct priority → +0.3
* ✅ Relevant reply → +0.3
* ❌ Incorrect actions → penalties

👉 Total reward is normalized between **0.0 and 1.0**

---

## 🧪 Tasks

The environment includes **3 tasks with increasing difficulty**:

### 🟢 Easy

* Simple classification (e.g., spam detection)

### 🟡 Medium

* Classification + priority assignment

### 🔴 Hard

* Full triage: classification + priority + contextual reply

Each task includes a **deterministic grader** ensuring reproducible evaluation.

---

## ⚙️ OpenEnv API

The environment follows the OpenEnv specification:

```python
reset() -> observation
step(action) -> observation, reward, done, info
state() -> current state
```

---

## 🤖 Baseline Inference

The project includes an `inference.py` script that:

* Uses OpenAI client (as required)
* Falls back to a rule-based agent if API is unavailable
* Produces reproducible scores

### 📌 Output Format

```
[START]
[STEP]
[END]
```

Fully compliant with hackathon requirements.

---

## 🐳 Deployment

The environment is deployed as a Docker-based Hugging Face Space.

### 🔗 Live Environment

👉 https://akashweb05-email-triage-env.hf.space

---

## 🛠️ Setup Instructions

### 1. Clone repository

```bash
git clone https://github.com/akashweb05/email-triage-env
cd email-triage-env
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run environment

```bash
python -m server.app
```

---

### 4. Run inference

```bash
python inference.py
```

---

## 🧩 Project Structure

```
email-triage-env/
│
├── env/
│   ├── environment.py
│   ├── models.py
│   └── tasks.py
│
├── server/
│   └── app.py
│
├── inference.py
├── openenv.yaml
├── Dockerfile
├── requirements.txt
├── pyproject.toml
└── uv.lock
```

---

## ✅ Compliance Checklist

* ✔ Real-world task simulation
* ✔ OpenEnv spec implemented
* ✔ 3+ tasks with graders
* ✔ Reward shaping
* ✔ Baseline inference script
* ✔ Dockerized deployment
* ✔ Hugging Face Space live

---

## 💡 Key Features

* Hybrid agent (LLM + rule-based fallback)
* Deterministic grading system
* Scalable environment design
* Fully reproducible evaluation

---

## 🏁 Future Improvements

* Multi-email thread handling
* Personalized user preferences
* Advanced NLP-based reply generation
* Integration with real email APIs

---

## 👨‍💻 Author

**Akashdeep Singh**

---

## 📄 License

MIT License
