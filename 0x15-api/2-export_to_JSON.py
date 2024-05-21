#!/usr/bin/python3
"""Defines a function that gathers progress data from an API"""
import csv
import json
import requests
import sys


def display_todo_progress(id):
    """Returns information about an employees todo list progress"""
    # Get the employee's name
    r = requests.get(f'https://jsonplaceholder.typicode.com/users?id={id}')
    name = r.json()[0].get('name')

    # Get the employee's todos
    r = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    completed = []
    for todo in r.json():
        if todo.get('completed'):
            completed.append(todo.get('title'))

    total = len(r.json())
    print(f'Employee {name} is done with tasks({len(completed)}/{total}):')

    # Print titles of completed todos
    for title in completed:
        print('\t', title)


def export_employee_todos_csv(id):
    """Records an employee's tasks in a csv file"""
    # Get the employees id and username
    r = requests.get(f'https://jsonplaceholder.typicode.com/users?id={id}')
    user_id = r.json()[0].get('id')
    user_name = r.json()[0].get('username')

    # Get the employee's todos
    r = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    todos = r.json()

    file_name = f'{id}.csv'

    # Write the employee's todos to a csv file
    with open(file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)

        # Go through all the todos of the employee
        for todo in todos:
            todo_status = todo.get('completed')
            todo_title = todo.get('title')
            # Create a todo row and write it to the file
            row = [user_id, user_name, todo_status, todo_title]
            writer.writerow(row)


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
