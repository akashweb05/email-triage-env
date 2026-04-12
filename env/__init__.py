"""
Email Triage OpenEnv Environment Package
Pattern: r-vb/bug-triage-env (successful OpenEnv submission)
"""

# Core environment
from env.environment import EmailTriageEnv

# Task definitions with explicit grader metadata
from env.tasks import (
    TASKS,
    TASK_LIST,
    TASK_COUNT,
    TASKS_WITH_GRADERS,
    GRADED_TASKS,
    NUM_TASKS_WITH_GRADERS,
    TASK_NAMES_WITH_GRADERS,
    GRADER_SPECS,
    SINGLE_GRADER_SPECS,
)

# All graders
from env.graders import (
    GRADERS,
    grade_easy_spam,
    grade_medium_meeting,
    grade_hard_multi,
    grade_support_request,
)

# Models
from env.models import (
    Observation,
    Action,
)

# Explicit exports for validator discovery
__all__ = [
    # Environment
    "EmailTriageEnv",
    # Tasks - dictionary and list
    "TASKS",
    "TASK_LIST",
    "TASK_COUNT",
    # Graders
    "GRADERS",
    "grade_easy_spam",
    "grade_medium_meeting",
    "grade_hard_multi",
    "grade_support_request",
    # Task grading metadata
    "GRADED_TASKS",
    "TASKS_WITH_GRADERS",
    "NUM_TASKS_WITH_GRADERS",
    "TASK_NAMES_WITH_GRADERS",
    "GRADER_SPECS",
    "SINGLE_GRADER_SPECS",
    # Models
    "Observation",
    "Action",
]

# Grading metadata exported at package level
GRADING_METADATA = {
    "num_graded_tasks": NUM_TASKS_WITH_GRADERS,
    "graded_task_names": TASK_NAMES_WITH_GRADERS,
    "all_tasks_graded": TASKS_WITH_GRADERS == TASK_COUNT,
    "graders": GRADERS,
    "grader_specs": GRADER_SPECS,
}





