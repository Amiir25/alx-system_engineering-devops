#!/usr/bin/env python3
'''
0-gather_data_from_an_api.py

Gather ingormation about TODO List progress of a user
'''

import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_api.py <ID>")
        exit(1)

    USER_DATA_API = "https://jsonplaceholder.typicode.com/users"
    TODO_LIST_API = "https://jsonplaceholder.typicode.com/todos"

    id = sys.argv[1]

    # GET request to fetch user data
    response = requests.get(f"{USER_DATA_API}/{id}")

    if response.status_code != 200:
        print(f"Error: Status code {response.status_code}")
    else:
        user_data = response.json()

    # Extract the name of the user
    user_name = user_data["name"]

    # GET request to fetch TODO List
    response = requests.get(f"{TODO_LIST_API}?userID={id}")

    if response.status_code != 200:
        print(f"Error: Status code {response.status_code}")
    else:
        todo_list = response.json()

    # Extract data from the TODO List
    TOTAL_NUMBER_OF_TASKS = len(todo_list)
    NUMBER_OF_DONE_TASKS = sum(1 for task in todo_list if task["completed"])
    TASK_TITLE = [task["title"] for task in todo_list if task["completed"]]

    # Print
    print(f"Employee {user_name} is done with tasks {NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}:")
    for i in range(NUMBER_OF_DONE_TASKS):
        print(f"\t {TASK_TITLE}")
