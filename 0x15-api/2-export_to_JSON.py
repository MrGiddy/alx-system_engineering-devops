#!/usr/bin/python3
"""Defines a function that gathers tasks data from an API"""
import json
import requests
import sys


def export_employee_todos_json(id):
    """Records an employee's tasks in json format"""
    # Get the employees id and username
    r = requests.get(f'https://jsonplaceholder.typicode.com/users?id={id}')
    user_id = r.json()[0].get('id')
    user_name = r.json()[0].get('username')

    # Get the employee's todos
    r = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    todos = r.json()

    tasks_list = []
    # Go through all the todos of the employee
    for todo in todos:
        todo_title = todo.get('title')
        todo_status = todo.get('completed')
        # Create a dictionary of a todo and append it to the tasks list
        task = {
                "task": todo_title,
                "completed": todo_status,
                "username": user_name
                }
        tasks_list.append(task)

    # Bind the list of all the todos of the employee to their id
    employee_todos = {
        user_id: tasks_list
    }

    file_name = f'{id}.json'

    # Save the employee's todos to .json file
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(employee_todos, f)


if __name__ == '__main__':
    id = int(sys.argv[1])
    export_employee_todos_json(id)
