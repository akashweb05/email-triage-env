# Email Triage Environment - Task Grading Documentation

## Overview

This environment includes **4 tasks with automatic grading**.

## Graded Tasks

| Task Name | Grader Function | Module | Score Range |
|-----------|-----------------|--------|------------|
| `easy_spam` | `grade_easy_spam` | `env.graders` | (0.005, 0.994) |
| `medium_meeting` | `grade_medium_meeting` | `env.graders` | (0.005, 0.994) |
| `hard_multi` | `grade_hard_multi` | `env.graders` | (0.005, 0.994) |
| `support_request` | `grade_support_request` | `env.graders` | (0.005, 0.994) |

## Accessing Graders

### Method 1: From env.tasks (Recommended)
```python
from env.tasks import TASKS, GRADED_TASKS

# TASKS list with graders attached
for task in TASKS:
    if "grader" in task:
        grader = task["grader"]
        # Call grader: grader(action, task["expected"])

# GRADED_TASKS explicit list
for task_info in GRADED_TASKS:
    print(task_info["name"], task_info["grader_function"])
```

### Method 2: From env.graders
```python
from env.graders import GRADERS, grade_easy_spam

# Access individual graders
grader_func = GRADERS["easy_spam"]
# or
grader_func = grade_easy_spam
```

### Method 3: From grader_registry (Root Level)
```python
from grader_registry import TASKS_WITH_GRADERS, GRADER_MAPPINGS

# List of tasks with graders
print(TASKS_WITH_GRADERS)  # ["easy_spam", "medium_meeting", "hard_multi", "support_request"]

# Get grader info
for task_name in TASKS_WITH_GRADERS:
    info = GRADER_MAPPINGS[task_name]
    print(f"{task_name}: {info['module']}.{info['function']}")
```

## Grader Specifications

All graders:
- Accept parameters: `action: Action`, `expected: dict`
- Return: `float` score strictly in range `(0, 1)` (not including 0 or 1)
- Clamp scores to safe bounds `[0.005, 0.994]` to prevent rounding issues

## Validation

Run the validation script to verify graders:
```bash
python validate.py
```

Expected output: All 4 tasks should show graders with valid scores in (0, 1).
