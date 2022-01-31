#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
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

    my_list = []
    for task in todos:
        if task['completed']:
            my_list.append(task)

    print("Employee {} is done with tasks({}/{}):".format(user[0]["name"],
          len(my_list), len(todos)))
    if len(my_list) > 0:
        for task in my_list:
            print("\t {}".format(task['title']))
