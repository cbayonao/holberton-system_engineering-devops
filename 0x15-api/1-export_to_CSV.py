#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    r = requests.get(url).json()
    USER_NAME = r.get('username')
    url2 = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(argv[1])
    req = requests.get(url2).json()
    USER_ID = argv[1]
    with open(USER_ID + ".csv", "w") as csvfile:
        file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in file:
            file.writerow([argv[1], USERNAME, i.get("completed"), i.get("title")])
