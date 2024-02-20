#!/usr/bin/python3
"""
Gather data from an API and export to CSV
"""

import csv
import json
import requests
from sys import argv

EMP_INFO_URL = 'https://jsonplaceholder.typicode.com/users/'
ALL_TODOS_URL = 'https://jsonplaceholder.typicode.com/todos'

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    emp_id = argv[1]
    emp_info_response = requests.get(EMP_INFO_URL + emp_id).json()
    all_todos_response = requests.get(ALL_TODOS_URL).json()

    todos_done_list = []
    with open('{}.csv'.format(emp_id), 'w', encoding="utf8", newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in all_todos_response:
            if todo['userId'] == int(emp_id):
                csv_writer.writerow(
                    [emp_id, emp_info_response['username'], str(todo['completed']), todo['title']])

    print("CSV file '{}.csv' has been created.".format(emp_id))
