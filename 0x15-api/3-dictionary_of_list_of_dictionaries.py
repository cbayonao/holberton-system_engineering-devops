#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
if __name__ == '__main__':
    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com/users'
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    rusers = requests.get(url).json()
    rtodos = requests.get(url2).json()
    my_dict = {j.get("id"): [{"task": i.get("title"),
                              "completed": i.get("completed"),
                              "username": j.get("username")} for i in rtodos
                             if i.get("userId") == j.get("id")]
               for j in rusers}
    print(type(my_dict))
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(my_dict, jsonfile)
