"""
Explicit Grader Registry - Top-level discoverable grader metadata.

This module provides an authoritative list of all tasks with graders.
It's designed to be easily discovered by validators and external tools.
"""

# Explicit list of task names that have graders
TASKS_WITH_GRADERS = [
    "easy_spam",
    "medium_meeting",
    "hard_multi",
    "support_request",
]

# Count of graded tasks for validator verification
NUM_TASKS_WITH_GRADERS = len(TASKS_WITH_GRADERS)

# Grader module and function names for each task
GRADER_MAPPINGS = {
    "easy_spam": {
        "module": "env.graders",
        "function": "grade_easy_spam",
    },
    "medium_meeting": {
        "module": "env.graders",
        "function": "grade_medium_meeting",
    },
    "hard_multi": {
        "module": "env.graders",
        "function": "grade_hard_multi",
    },
    "support_request": {
        "module": "env.graders",
        "function": "grade_support_request",
    },
}

def get_grader_info(task_name: str):
    """Get grader module and function name for a task."""
    return GRADER_MAPPINGS.get(task_name)

def has_grader(task_name: str) -> bool:
    """Check if a task has a grader."""
    return task_name in TASKS_WITH_GRADERS

if __name__ == "__main__":
    print(f"Total tasks with graders: {NUM_TASKS_WITH_GRADERS}")
    print("\nGrader Registry:")
    for task_name in TASKS_WITH_GRADERS:
        info = get_grader_info(task_name)
        print(f"  {task_name}: {info['module']}.{info['function']}")
