#!/usr/bin/python3
"""Get the todo list for one user and print info"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    resp = requests.get(url)
    tasks = resp.json()
    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    resp = requests.get(url)
    user = resp.json()

    total = 0
    done = 0
    for task in tasks:
        if task.get("completed"):
            done += 1
        total += 1

    tasks = [t for t in tasks if t.get("completed")]
    name = user.get("name")
    if name is None:
        exit()
    
    # Format the output message with a fixed length for the employee name
    output_message = "Employee {} is done with tasks({}/{}):".format(name.ljust(25), done, total)
    
    print(output_message)
    
    for task in tasks:
        print("\t " + task.get("title"))
