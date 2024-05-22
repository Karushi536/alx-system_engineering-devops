#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response = requests.get(url)
    tasks = response.json()

    if not tasks:
        print("No tasks found for employee with ID {}".format(employee_id))
        exit(0)

    user_info_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_info_response = requests.get(user_info_url)
    user_info = user_info_response.json()
    username = user_info.get('username')

    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([employee_id, username, task['completed'], task['title']])
