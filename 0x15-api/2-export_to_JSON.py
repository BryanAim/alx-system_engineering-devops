#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import json
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
        my_dict = {}
        my_dict["task"] = task['title']
        my_dict["completed"] = task['completed']
        my_dict["username"] = user[0]['username']
        my_list.append(my_dict)
    json_obj = {}
    json_obj[sys.argv[1]] = my_list
    with open("{}.json".format(sys.argv[1]), 'w') as jsonfile:
        json.dump(json_obj, jsonfile)
