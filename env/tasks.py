"""
Tasks for Email Triage OpenEnv environment.
Each task has a grader function with explicit metadata for validator discovery.
Pattern from successful OpenEnv submission: r-vb/bug-triage-env
"""

from env.graders import GRADERS

# Task definitions with explicit grader specifications
TASKS_DICT = {
    "easy_spam": {
        "id": "easy_spam",
        "name": "Easy Spam Classification",
        "difficulty": "easy",
        "email": "Win a free iPhone!!! Click here!!!",
        "expected": {
            "label": "spam",
            "priority": 1,
            "requires": ["spam", "free", "click"]
        },
        "description": "Straightforward spam email classification task",
        "n_issues": 1,
        "expected_score_range": [0.8, 1.0],
        "success_criteria": "Correctly classify spam with keyword matching",
        "grader": GRADERS["easy_spam"],
        "grader_spec": {
            "name": "grade_easy_spam",
            "type": "python_function",
            "entrypoint": "env.graders:grade_easy_spam",
            "deterministic": True,
            "score_range": [0.0, 1.0],
        },
        "graders": [
            {
                "name": "grade_easy_spam",
                "type": "python_function",
                "entrypoint": "env.graders:grade_easy_spam",
                "deterministic": True,
                "score_range": [0.0, 1.0],
            }
        ],
        "has_grader": True,
    },
    "medium_meeting": {
        "id": "medium_meeting",
        "name": "Medium Meeting Classification",
        "difficulty": "medium",
        "email": "Client meeting tomorrow at 10 AM",
        "expected": {
            "label": "important",
            "priority": 4,
            "requires": ["meeting", "tomorrow"]
        },
        "description": "Business meeting email requiring temporal reasoning",
        "n_issues": 1,
        "expected_score_range": [0.6, 0.95],
        "success_criteria": "Identify business meetings and set appropriate priority",
        "grader": GRADERS["medium_meeting"],
        "grader_spec": {
            "name": "grade_medium_meeting",
            "type": "python_function",
            "entrypoint": "env.graders:grade_medium_meeting",
            "deterministic": True,
            "score_range": [0.0, 1.0],
        },
        "graders": [
            {
                "name": "grade_medium_meeting",
                "type": "python_function",
                "entrypoint": "env.graders:grade_medium_meeting",
                "deterministic": True,
                "score_range": [0.0, 1.0],
            }
        ],
        "has_grader": True,
    },
    "hard_multi": {
        "id": "hard_multi",
        "name": "Hard Multi-Intent Classification",
        "difficulty": "hard",
        "email": "I have a billing issue and want to schedule a call",
        "expected": {
            "label": "important",
            "priority": 5,
            "requires": ["billing", "call"]
        },
        "description": "Complex email with multiple intents requiring synthesis",
        "n_issues": 1,
        "expected_score_range": [0.5, 0.85],
        "success_criteria": "Handle multiple intents and synthesize appropriate response",
        "grader": GRADERS["hard_multi"],
        "grader_spec": {
            "name": "grade_hard_multi",
            "type": "python_function",
            "entrypoint": "env.graders:grade_hard_multi",
            "deterministic": True,
            "score_range": [0.0, 1.0],
        },
        "graders": [
            {
                "name": "grade_hard_multi",
                "type": "python_function",
                "entrypoint": "env.graders:grade_hard_multi",
                "deterministic": True,
                "score_range": [0.0, 1.0],
            }
        ],
        "has_grader": True,
    },
    "support_request": {
        "id": "support_request",
        "name": "Support Request Classification",
        "difficulty": "hard",
        "email": "My account is locked, please help",
        "expected": {
            "label": "important",
            "priority": 5,
            "requires": ["account", "help"]
        },
        "description": "Urgent support request requiring immediate attention",
        "n_issues": 1,
        "expected_score_range": [0.7, 1.0],
        "success_criteria": "Escalate account issues to highest priority",
        "grader": GRADERS["support_request"],
        "grader_spec": {
            "name": "grade_support_request",
            "type": "python_function",
            "entrypoint": "env.graders:grade_support_request",
            "deterministic": True,
            "score_range": [0.0, 1.0],
        },
        "graders": [
            {
                "name": "grade_support_request",
                "type": "python_function",
                "entrypoint": "env.graders:grade_support_request",
                "deterministic": True,
                "score_range": [0.0, 1.0],
            }
        ],
        "has_grader": True,
    },
}

# Ensure all tasks have graders attached
for task_id, task in TASKS_DICT.items():
    if "grader" not in task and task_id in GRADERS:
        task["grader"] = GRADERS[task_id]

# Task list for ordered access (like r-vb pattern)
TASK_LIST = list(TASKS_DICT.values())

# Count tasks with graders (explicit for validator)
TASKS_WITH_GRADERS = sum(1 for task in TASKS_DICT.values() if callable(task.get("grader")))

# Grader specifications for server endpoints
GRADER_SPECS = {
    task_id: task.get("graders", [])
    for task_id, task in TASKS_DICT.items()
}

SINGLE_GRADER_SPECS = {
    task_id: task.get("grader_spec")
    for task_id, task in TASKS_DICT.items()
}

# Legacy compatibility exports
GRADED_TASKS = [
    {
        "name": TASKS_DICT[task_id]["name"],
        "task_id": task_id,
        "grader_function": TASKS_DICT[task_id]["grader"],
        "grader_name": TASKS_DICT[task_id]["grader_spec"]["name"],
        "difficulty": TASKS_DICT[task_id]["difficulty"],
    }
    for task_id in TASKS_DICT.keys()
    if callable(TASKS_DICT[task_id].get("grader"))
]

# Number of tasks with graders
NUM_TASKS_WITH_GRADERS = TASKS_WITH_GRADERS

# List of task names that are graded
TASK_NAMES_WITH_GRADERS = [task["id"] for task in TASK_LIST if callable(task.get("grader"))]

# Total task count
TASK_COUNT = len(TASKS_DICT)

# CRITICAL: Create TASKS that validators can access multiple ways
# Some validators iterate: for task in TASKS (expects list-like)
# Some validators use: TASKS[task_id] (expects dict-like)
# Solution: make TASKS = TASK_LIST but also keep TASKS_DICT accessible

# Use TASK_LIST as the primary TASKS export (works with iteration)
TASKS = TASK_LIST

# Export both dict and list versions for different access patterns
# Dict for lookup by task_id
TASKS_BY_ID = TASKS_DICT
