#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    r = requests.get(url).json()
    EMPLOYEE_NAME = r.get('name')
    url2 = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(argv[1])
    req = requests.get(url2).json()
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    for task in req:
        if task.get("completed") is True:
            TASK_TITLE.append(task.get("title"))
            NUMBER_OF_DONE_TASKS += 1
    TOTAL_NUMBER_OF_TASKS = len(req)
    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task2 in TASK_TITLE:
        print("\t {}".format(task2))
