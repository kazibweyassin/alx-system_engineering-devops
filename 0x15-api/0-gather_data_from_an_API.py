#!/usr/bin/python3
"""Get the todo list for one user and print info"""

import requests
from sys import argv

if __name__ == "__main__":
    try:
        user_id = argv[1]
    except IndexError:
        print("Please provide a user ID as a command-line argument.")
        exit()

    url = "https://jsonplaceholder.typicode.com/todos?userId=" + user_id
    resp = requests.get(url)
    tasks = resp.json()
    url = "https://jsonplaceholder.typicode.com/users/" + user_id
    resp = requests.get(url)
    user = resp.json()

    total = 0
    done = 0
    for task in tasks:
        if task.get("completed"):
            done = done + 1
        total = total + 1

    tasks = [t for t in tasks if t.get("completed")]
    name = user.get("name")
    if name is None:
        exit()
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for task in tasks:
        print("\t " + task.get("title"))