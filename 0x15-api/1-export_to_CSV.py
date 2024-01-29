#!/usr/bin/python3
"""Export the data to a CSV file"""
import csv
import requests
import sys

def export_to_csv(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user information
    user_response = requests.get(base_url + "users/{}".format(employee_id))
    user_data = user_response.json()
    
    # Fetch TODO list for the employee
    todo_response = requests.get(base_url + "todos", params={"userId": employee_id})
    todo_data = todo_response.json()

    # Extract relevant information
    username = user_data.get("username")
    csv_data = [
        [employee_id, username, task.get("completed"), task.get("title")]
        for task in todo_data
    ]

    # Write data to CSV file
    with open("{}.csv".format(employee_id), "w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)

if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Get the employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    # Call the function to export data to CSV
    export_to_csv(employee_id)
