from env import TASKS
print('TASKS count', len(TASKS))
print('All tasks have grader', all('grader' in t for t in TASKS))
print('TASKS names', [t['name'] for t in TASKS])
for task in TASKS:
    print(task['name'], task['grader'].__name__)
