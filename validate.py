"""
Validation entry point for OpenEnv validator.

This module provides functions that openenv validate can call to discover
and verify tasks with graders.
"""

from env import TASKS, GRADERS
from env.models import Action


def get_graded_tasks():
    """Return list of task names that have graders.
    
    This is called by openenv validate to discover graded tasks.
    """
    return [task["name"] for task in TASKS if "grader" in task]


def validate_graders():
    """Validate that all tasks with graders return valid scores.
    
    Returns:
        dict: Validation results
    """
    results = {
        "total_tasks": len(TASKS),
        "tasks_with_graders": 0,
        "all_scores_valid": True,
        "tasks": []
    }
    
    for task in TASKS:
        if "grader" not in task:
            continue
        
        results["tasks_with_graders"] += 1
        grader = task["grader"]
        
        # Test with a valid action
        try:
            test_action = Action(
                label=task["expected"]["label"],
                priority=task["expected"]["priority"],
                reply=" ".join(task["expected"].get("requires", []))
            )
            score = grader(test_action, task["expected"])
            
            score_valid = 0 < score < 1
            if not score_valid:
                results["all_scores_valid"] = False
            
            results["tasks"].append({
                "name": task["name"],
                "grader": grader.__name__,
                "test_score": float(score),
                "score_valid": score_valid
            })
        except Exception as e:
            results["all_scores_valid"] = False
            results["tasks"].append({
                "name": task["name"],
                "grader": grader.__name__,
                "error": str(e)
            })
    
    results["validation_passed"] = (
        results["tasks_with_graders"] >= 3 and
        results["all_scores_valid"]
    )
    
    return results


if __name__ == "__main__":
    import json
    results = validate_graders()
    print(json.dumps(results, indent=2))
    
    if results["validation_passed"]:
        print("\n✓ Validation PASSED")
        exit(0)
    else:
        print("\n✗ Validation FAILED")
        exit(1)
