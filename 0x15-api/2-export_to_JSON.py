#!/usr/bin/python3
"""
This script retrieves and exports information about an employee's
TODO list progress in JSON format using a REST API.
"""

import json
from sys import argv
import requests  # Import requests alphabetically

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

        employee_name = user_response.get('username')
        json_filename = "{}.json".format(employee_id)

        tasks_list = []
        for task in tasks_response:
            task_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            }
            tasks_list.append(task_data)

        employee_data = {str(employee_id): tasks_list}

        with open(json_filename, mode='w') as jsonfile:
            json.dump(employee_data, jsonfile)

        print("JSON file '{}' has been created.".format(json_filename))

    except requests.exceptions.RequestException as e:
        print("Error:", e)
