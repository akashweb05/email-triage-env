TASKS = [
    {
        "name": "easy_spam",
        "email": "Win a free iPhone!!! Click here!!!",
        "expected": {
            "label": "spam",
            "priority": 1
        }
    },
    {
        "name": "medium_meeting",
        "email": "Client meeting tomorrow at 10 AM",
        "expected": {
            "label": "important",
            "priority": 5
        }
    },
    {
        "name": "hard_multi",
        "email": "I have a billing issue and want to schedule a call",
        "expected": {
            "label": "important",
            "priority": 5
        }
    }
]