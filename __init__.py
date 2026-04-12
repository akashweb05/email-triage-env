"""
Root-level module for email-triage-env package.
Provides easy access to all environment components and grader metadata.
"""

# Export everything from env package
from env import (
    EmailTriageEnv,
    Observation,
    Action,
    TASKS,
    GRADED_TASKS,
    NUM_TASKS_WITH_GRADERS,
    TASK_NAMES_WITH_GRADERS,
    GRADERS,
    grade_easy_spam,
    grade_medium_meeting,
    grade_hard_multi,
    grade_support_request,
)

# Explicit metadata for graders
GRADING_METADATA = {
    "enabled": True,
    "total_tasks": 4,
    "tasks_with_graders": NUM_TASKS_WITH_GRADERS,
    "task_names": TASK_NAMES_WITH_GRADERS,
    "tasks": GRADED_TASKS,
    "minimum_required": 3,
    "status": "valid"
}

__all__ = [
    "EmailTriageEnv",
    "Observation",
    "Action",
    "TASKS",
    "GRADED_TASKS",
    "NUM_TASKS_WITH_GRADERS",
    "TASK_NAMES_WITH_GRADERS",
    "GRADERS",
    "GRADING_METADATA",
    "grade_easy_spam",
    "grade_medium_meeting",
    "grade_hard_multi",
    "grade_support_request",
]
