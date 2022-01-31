#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import csv
import requests
import sys


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/todos'
    params = (('userId', sys.argv[1]),)
    req_todo = requests.get(url, params=params)
    todos = req_todo.json()

    url = 'https://jsonplaceholder.typicode.com/users'
    params = (('id', sys.argv[1]),)
    req_user = requests.get(url, params=params)
    user = req_user.json()

    with open("{}.csv".format(sys.argv[1]), 'w', newline='') as csvfile:
        cvs_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            cvs_writer.writerow([int(sys.argv[1]), user[0]['username'],
                                 task['completed'], task['title']])
