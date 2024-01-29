#!/usr/bin/python3
"""Exports all employee to-do list data in JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    all_employees_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in requests.get(url + "todos", params={"userId": user_id}).json()
        ]

        all_employees_tasks[user_id] = tasks
        
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employees_tasks, jsonfile)
