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
    req_todo = requests.get(url)
    todos = req_todo.json()

    url = 'https://jsonplaceholder.typicode.com/users'
    req_user = requests.get(url)
    users = req_user.json()

    user_dict = {}

    for user in users:
        username = user['username']
        user_info = []

        for task in todos:
            if task['userId'] == user['id']:
                dict_info = {}
                dict_info['username'] = username
                dict_info['task'] = task['title']
                dict_info['completed'] = task['completed']
                user_info.append(dict_info)
        user_dict[user['id']] = user_info

    with open("todo_all_employees.json", 'w') as f:
        json.dump(user_dict, f)
