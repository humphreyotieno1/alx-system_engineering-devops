#!/usr/bin/python3
"""Export the data to a CSV file"""
import csv
import requests
import sys


if __name__ == '__main__':
    baseUrl = "https://jsonplaceholder.typicode.com/"
    user = requests.get(baseUrl + "user/{}".format(sys.argv[1])).json()
    username = user.get("username")
    to_do = requests.get(baseUrl + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(sys.argv[1]), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        [writer.writerow(
            [sys.argv[1], username, task.get("completed"), task.get("title")]
            ) for task in to_do]
