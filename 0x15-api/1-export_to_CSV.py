#!/usr/bin/python3
"""Get data from an API and export to CSV."""
import csv
from sys import argv
import requests

def gather_and_export_to_csv(user_id):
    """Fetches and exports data from an API to CSV."""
    # Fetch TODO list for the user
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todo_response = requests.get(todo_url)
    tasks = todo_response.json()

    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    user = user_response.json()

    name = user.get("name")
    if name is None:
        exit()

    # Create CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        fidnam = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fidnam)

        # Write CSV header
        csv_writer.writeheader()

        # Write tasks to CSV
        for task in tasks:
            csv_writer.writerow({
                'USER_ID': user_id,
                'USERNAME': name,
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })

        print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    # Check if a user ID is provided as a command-line argument
    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = argv[1]
    gather_and_export_to_csv(user_id)

