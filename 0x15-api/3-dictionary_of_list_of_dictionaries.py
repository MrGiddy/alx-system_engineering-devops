#!/usr/bin/python3
"""Defines a function that gathers tasks data from an API"""
import json
import requests


def get_employee_todos(id):
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

    return tasks_list


def export_all_employees_todos_json():
    """Record all tasks of all employees in a .json file"""
    r = requests.get(f'https://jsonplaceholder.typicode.com/users')

    todos_collection = {}

    # For each employee in the response
    for employee in r.json():
        # Retrieve the tasks of the employee
        id = employee.get('id')
        tasks_list = get_employee_todos(id)
        # Add the tasks of the employee to the todos collection
        todos_collection[id] = tasks_list

    file_name = 'todo_all_employees.json'

    # Save the collection of employee's todos to a .json file
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(todos_collection, f)


if __name__ == '__main__':
    export_all_employees_todos_json()
