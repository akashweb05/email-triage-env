from env.graders import GRADERS

TASKS = [
    {
        "name": "easy_spam",
        "email": "Win a free iPhone!!! Click here!!!",
        "expected": {
            "label": "spam",
            "priority": 1,
            "requires": ["spam", "free", "click"]
        },
        "grader": GRADERS["easy_spam"]
    },
    {
        "name": "medium_meeting",
        "email": "Client meeting tomorrow at 10 AM",
        "expected": {
            "label": "important",
            "priority": 4,
            "requires": ["meeting", "tomorrow"]
        },
        "grader": GRADERS["medium_meeting"]
    },
    {
        "name": "hard_multi",
        "email": "I have a billing issue and want to schedule a call",
        "expected": {
            "label": "important",
            "priority": 5,
            "requires": ["billing", "call"]
        },
        "grader": GRADERS["hard_multi"]
    },
    {
        "name": "support_request",
        "email": "My account is locked, please help",
        "expected": {
            "label": "important",
            "priority": 5,
            "requires": ["account", "help"]
        },
        "grader": GRADERS["support_request"]
    }
]

# Explicit export for validator discovery
GRADED_TASKS = [
    {
        "name": "easy_spam",
        "grader_function": GRADERS["easy_spam"],
        "grader_name": "grade_easy_spam",
    },
    {
        "name": "medium_meeting",
        "grader_function": GRADERS["medium_meeting"],
        "grader_name": "grade_medium_meeting",
    },
    {
        "name": "hard_multi",
        "grader_function": GRADERS["hard_multi"],
        "grader_name": "grade_hard_multi",
    },
    {
        "name": "support_request",
        "grader_function": GRADERS["support_request"],
        "grader_name": "grade_support_request",
    },
]