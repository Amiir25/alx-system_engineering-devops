#!/usr/bin/python3
'''
3-dictionary_of_list_of_dictionaries.py

This script records all tasks of all users and exports in a JSON format
'''

import json
import requests


if __name__ == "__main__":

    USER_DATA_API = "https://jsonplaceholder.typicode.com/users"
    TODO_LIST_API = "https://jsonplaceholder.typicode.com/todos"

    # GET request to fetch all users
    user_response = requests.get(USER_DATA_API)

    if user_response.status_code != 200:
        print(f"Error: Status code {response.status_code}")
        exit(1)
    else:
        users = user_response.json()

    # Dictionary to hold all employee task
    all_tasks = {}

    # Loop to fetch all users' tasks
    for user in users:
        user_id = user["id"]
        username = user["username"]

        # Get request to fetch the TODO List of the 'user'
        todo_response = requests.get(f"{TODO_LIST_API}?userId={user_id}")
        if todo_response.status_code != 200:
            print(f"Error: Status code {response.status_code}")

        todo_list = todo_response.json()

        # Store the tasks of 'user' in dictionary
        all_tasks[str(user_id)] = [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            }
            for task in todo_list
        ]

    # Create the JSON file
    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as file:
        json.dump(all_tasks, file)
