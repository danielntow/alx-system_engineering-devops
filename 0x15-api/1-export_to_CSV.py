#!/usr/bin/python3
"""gather data from an API"""
import csv
import json
import requests
from sys import argv

emp_info = 'https://jsonplaceholder.typicode.com/users/'
all_todos = 'https://jsonplaceholder.typicode.com/todos'
if __name__ == "__main__":
    emp_id = argv[1]
    get_emp_info = json.loads(requests.get(emp_info + emp_id).text)
    get_all_todos = json.loads(requests.get(all_todos).text)
    todos_done_list = []
    name = None

    with open('{}.csv'.format(emp_id), 'w', encoding="utf8") as f:
        for i in get_all_todos:
            if i['userId'] == int(emp_id):
                f.write('"{}","{}","{}","{}"\n'.format(
                    emp_id, get_emp_info['username'],
                    i['completed'], i['title']))
