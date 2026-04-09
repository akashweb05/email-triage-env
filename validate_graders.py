#!/usr/bin/env python
"""Validate that all tasks have graders and scores are strictly in (0, 1)."""

from env import TASKS, GRADERS
from env.models import Action

print("=" * 60)
print("TASK AND GRADER VALIDATION")
print("=" * 60)

print(f"\nTotal tasks: {len(TASKS)}")
print(f"Total graders: {len(GRADERS)}")

for i, task in enumerate(TASKS):
    print(f"\n--- Task {i+1}: {task['name']} ---")
    print(f"  Has 'grader' key: {'grader' in task}")
    
    if 'grader' in task:
        grader = task['grader']
        print(f"  Grader callable: {callable(grader)}")
        print(f"  Grader name: {grader.__name__ if hasattr(grader, '__name__') else 'N/A'}")
        
        # Test with perfect match action
        perfect_action = Action(
            label=task['expected']['label'],
            priority=task['expected']['priority'],
            reply=" ".join(task['expected'].get('requires', []))
        )
        
        perfect_score = grader(perfect_action, task['expected'])
        print(f"  Perfect score: {perfect_score:.6f}")
        print(f"  Valid (0 < score < 1): {0 < perfect_score < 1}")
        
        # Test with worst match action
        worst_action = Action(
            label='promo',
            priority=3,
            reply='hello'
        )
        
        worst_score = grader(worst_action, task['expected'])
        print(f"  Worst score: {worst_score:.6f}")
        print(f"  Valid (0 < score < 1): {0 < worst_score < 1}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

# Check if all tasks have graders
all_have_graders = all('grader' in task for task in TASKS)
print(f"All {len(TASKS)} tasks have graders: {all_have_graders}")

# Test all graders with various inputs
test_cases = [
    ("Perfect match", lambda t: Action(
        label=t['expected']['label'],
        priority=t['expected']['priority'],
        reply=" ".join(t['expected'].get('requires', []))
    )),
    ("Partial match", lambda t: Action(
        label=t['expected']['label'],
        priority=t['expected']['priority'],
        reply="hello"
    )),
    ("No match", lambda t: Action(
        label='promo',
        priority=2,
        reply="nope"
    )),
]

all_valid = True
for case_name, action_fn in test_cases:
    print(f"\nTest case: {case_name}")
    for task in TASKS:
        if 'grader' in task:
            action = action_fn(task)
            score = task['grader'](action, task['expected'])
            valid = 0 < score < 1
            all_valid = all_valid and valid
            status = "✓" if valid else "✗"
            print(f"  {task['name']}: {score:.6f} {status}")

print("\n" + "=" * 60)
if all_valid and all_have_graders and len(TASKS) >= 3:
    print("✓ ALL CHECKS PASSED")
else:
    print("✗ VALIDATION FAILED")
    if not all_have_graders:
        print("  - Not all tasks have graders")
    if not all_valid:
        print("  - Some scores are out of valid range")
    if len(TASKS) < 3:
        print(f"  - Only {len(TASKS)} tasks (need at least 3)")
print("=" * 60)
