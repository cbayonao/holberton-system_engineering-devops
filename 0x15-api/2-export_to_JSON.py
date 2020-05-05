#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    r = requests.get(url).json()
    USERNAME = r.get('username')
    url2 = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(argv[1])
    req = requests.get(url2).json()
    USER_ID = argv[1]
    my_dict = {}
    my_dict[USER_ID] = [{"task": i.get("title"),
                         "completed": i.get("completed"),
                         "username": USERNAME} for i in req]
    with open(USER_ID + ".json", "w") as jsonfile:
        json.dump(my_dict, jsonfile)
