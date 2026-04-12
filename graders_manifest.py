"""
Graders Module - Discoverable entry point for task graders.

Exposes all task graders with clear metadata for validators.
This module provides an easy-to-discover interface for checking
which tasks have graders and accessing them.
"""

from env.graders import (
    grade_easy_spam,
    grade_medium_meeting,
    grade_hard_multi,
    grade_support_request,
)

# List of all available graders
AVAILABLE_GRADERS = {
    "easy_spam": grade_easy_spam,
    "medium_meeting": grade_medium_meeting,
    "hard_multi": grade_hard_multi,
    "support_request": grade_support_request,
}

# Number of graded tasks
NUM_GRADED_TASKS = len(AVAILABLE_GRADERS)

def get_grader(task_name: str):
    """Get grader function for a task by name.
    
    Args:
        task_name: Name of the task (e.g., 'easy_spam')
        
    Returns:
        Grader function if found, None otherwise
    """
    return AVAILABLE_GRADERS.get(task_name)

def list_graded_tasks():
    """Return list of all task names that have graders."""
    return list(AVAILABLE_GRADERS.keys())

if __name__ == "__main__":
    print("Available Graders:")
    for task_name, grader_func in AVAILABLE_GRADERS.items():
        print(f"  - {task_name}: {grader_func.__name__}")
    print(f"\nTotal graded tasks: {NUM_GRADED_TASKS}")
