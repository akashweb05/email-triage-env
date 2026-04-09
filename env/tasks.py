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