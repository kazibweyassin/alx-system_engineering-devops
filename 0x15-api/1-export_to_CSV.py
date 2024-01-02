#!/usr/bin/env python3
"""Gather data from an API"""

import requests
from sys import argv
import json

def main():
    """Gather data from an API"""
    
    userID = argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(userID)
    todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(userID)
    name = requests.get(user).json().get('name')
    tasks = requests.get(todo).json()
    total_tasks = len(tasks)
    completed_tasks = 0
    for task in tasks:
        if task.get('completed') is True:
            completed_tasks += 1
    print('Employee {} is done with tasks({}/{}):'.format(name, completed_tasks, total_tasks))
    for task in tasks:
        if task.get('completed') is True:
            print('\t {}'.format(task.get('title')))
            
    with open('{}.csv'.format(userID), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'.format(userID, name, task.get('completed'), task.get('title')))
            
            
if __name__ == "__main__":
    if len(argv) == 2:
        main()