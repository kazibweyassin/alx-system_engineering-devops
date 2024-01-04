#!/usr/bin/python3
"""Get data from an API."""
from sys import argv
import requests


def gather_data_from_api(user_id):
    """Fetches and prints data from an API."""
    # Fetch TODO list for the user
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todo_response = requests.get(todo_url)
    tasks = todo_response.json()

    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    user = user_response.json()

    total = len(tasks)
    done = sum(task.get("completed", False) for task in tasks)

    # Filter completed tasks
    completed_tasks_list = [task for task in tasks if task.get("completed")]

    name = user.get("name")
    if name is None:
        exit()

    # Format the output message with a fixed length for the employee name
    out_mesg = f"Employee {name.ljust(25)} is done with tasks({done}/{total}):"
    print(out_mesg)

    # Display titles of completed tasks
    for task in completed_tasks_list:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    # Check if a user ID is provided as a command-line argument
    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = argv[1]
    gather_data_from_api(user_id)
