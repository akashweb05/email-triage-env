TASKS = [
    {
        "name": "easy_spam",
        "email": "Win a free iPhone!!! Click here!!!",
        "expected": {
            "label": "spam",
            "priority": 1,
            "requires": []
        }
    },
    {
        "name": "medium_meeting",
        "email": "Client meeting tomorrow at 10 AM",
        "expected": {
            "label": "important",
            "priority": 5,
            "requires": []
        }
    },
    {
        "name": "hard_multi",
        "email": "I have a billing issue and want to schedule a call",
        "expected": {
            "label": "important",
            "priority": 5,
            "requires": ["sorry", "call"]
        }
    },
    {
        "name": "support_request",
        "email": "My account is locked, please help",
        "expected": {
            "label": "important",
            "priority": 5,
            "requires": ["sorry", "help"]
        }
    }
]
