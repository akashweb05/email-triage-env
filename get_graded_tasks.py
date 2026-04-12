#!/usr/bin/env python
"""
Get graded tasks - entry point that validators might call.
This script outputs information about graded tasks in a format validators expect.
"""

import sys
import json

try:
    from env.environment import EmailTriageEnv
    
    # Get graded tasks from the environment class
    env_class = EmailTriageEnv
    
    result = {
        "success": True,
        "environment": "email-triage-env",
        "graded_tasks": env_class.GRADED_TASK_NAMES,
        "num_graded_tasks": env_class.NUM_GRADED_TASKS,
        "graders": {
            name: grader.__name__ 
            for name, grader in env_class.GRADERS.items()
        },
        "tasks": [
            {
                "name": task["name"],
                "has_grader": "grader" in task,
                "grader_function": task["grader"].__name__ if "grader" in task else None,
            }
            for task in env_class.TASKS
        ]
    }
    
    print(json.dumps(result, indent=2))
    sys.exit(0)
    
except Exception as e:
    result = {
        "success": False,
        "error": str(e)
    }
    print(json.dumps(result, indent=2), file=sys.stderr)
    sys.exit(1)
