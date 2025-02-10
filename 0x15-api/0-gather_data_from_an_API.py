#!/usr/bin/env python3
'''
0-gather_data_from_an_api.py

Gather information about TODO List progress of a user
'''

import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_api.py <ID>")
        exit(1)

    USER_DATA_API = "https://jsonplaceholder.typicode.com/users"
    TODO_LIST_API = "https://jsonplaceholder.typicode.com/todos"

    id = int(sys.argv[1])

    # GET request to fetch user data
    user_response = requests.get(f"{USER_DATA_API}/{id}")

    if user_response.status_code != 200:
        print(f"Error: Status code {response.status_code}")
        exit(1)
    else:
        user_data = user_response.json()

    # Extract the name of the user
    user_name = user_data["name"]

    # GET request to fetch TODO List
    todo_response = requests.get(f"{TODO_LIST_API}?userId={id}")

    if todo_response.status_code != 200:
        print(f"Error: Status code {response.status_code}")
        exit(1)
    else:
        todo_list = todo_response.json()

    # Extract data from the TODO List
    TOTAL_NUMBER_OF_TASKS = len(todo_list)
    TASK_TITLE = [task["title"] for task in todo_list if task["completed"]]
    NUMBER_OF_DONE_TASKS = len(TASK_TITLE)

    # Print
    print(f"Employee {user_name} is done with tasks {
        NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}: ")
    for task in TASK_TITLE:
        print(f"\t {task}")
