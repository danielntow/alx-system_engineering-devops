#!/usr/bin/python3
"""
This script retrieves and displays information about an
employee's TODO list progress using a REST API.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    try:
        user_response = requests.get(user_url).json()
        tasks_response = requests.get(tasks_url).json()

        employee_name = user_response.get('name')
        total_tasks = len(tasks_response)
        completed_tasks = [
            task for task in tasks_response if task.get('completed')]
        num_completed_tasks = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(employee_name,
              num_completed_tasks, total_tasks))

        for task in completed_tasks:
            print("\t {}".format(task.get('title')))

    except requests.exceptions.RequestException as e:
        print("Error:", e)
