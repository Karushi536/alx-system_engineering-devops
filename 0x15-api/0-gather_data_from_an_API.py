#!/usr/bin/python3
import requests
import sys

def get_todo_list_progress(employee_id):
    """
    Get the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Make API request to get employee data
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()
    employee_name = employee_data.get("name", "Unknown")

    # Make API request to get todo list data
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_list_data = response.json()

    # Calculate number of done tasks
    done_tasks = [task for task in todo_list_data if task.get("completed", False)]
    num_done_tasks = len(done_tasks)
    total_num_tasks = len(todo_list_data)

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_num_tasks}):")
    for task in done_tasks:
        print(f"\t{task.get('title', 'Unknown')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
