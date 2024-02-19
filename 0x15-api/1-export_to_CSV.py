#!/usr/bin/python3
"""
This script retrieves and exports information about an employee's
n TODO list progress in CSV format using a REST API.
"""

import csv
from sys import argv
import requests

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
        csv_filename = "{}.csv".format(employee_id)

        with open(csv_filename, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in tasks_response:
                csv_writer.writerow(
                    [employee_id, employee_name, str(
                        task['completed']), task['title']])

    except requests.exceptions.RequestException as e:
        print("Error:", e)
