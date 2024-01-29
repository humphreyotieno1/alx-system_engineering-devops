#!/usr/bin/python3
"""Export the data to a JSON file"""
import json
import requests
import sys


def export_to_json(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    
    user_response = requests.get(base_url + "users/{}".format(employee_id))
    user_data = user_response.json()
    
    todo_response = requests.get(base_url + "todos", params={"userId": employee_id})
    todo_data = todo_response.json()

    username = user_data.get("username")
    json_data = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            for task in todo_data
        ]
    }

    file_json = "{}.json".format(employee_id)
    with open(file_json, 'w') as f:
        json.dump(json_data, f)

if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    export_to_json(employee_id)
