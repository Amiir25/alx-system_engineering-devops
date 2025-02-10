#!/usr/bin/python3
'''
2-export_to_JSON.py

Exports API data in a JSON format
'''

import json
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

    # Extract the username
    username = user_data["username"]

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
    TASK_COMPLETED_STATUS = [task["completed"] for task in todo_list]

    # Create the JSON file
    file_name = f"{id}.json"
    data = {
        str(id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            }
            for task in todo_list
        ]
    }
    with open(file_name, mode='w') as file:
        json.dump(data, file)
