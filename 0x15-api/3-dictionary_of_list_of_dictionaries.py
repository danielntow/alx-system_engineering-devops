#!/usr/bin/python3
"""
Export data in JSON format
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    user_dict = {}
    for user in users:
        user_id = str(user['id'])
        user_tasks = []
        tasks_url = f"{url}/{user_id}/todos"
        tasks_response = requests.get(tasks_url)
        tasks = tasks_response.json()

        for task in tasks:
            task_dict = {
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            }
            user_tasks.append(task_dict)

        user_dict[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_dict, json_file)
