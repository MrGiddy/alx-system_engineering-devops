#!/usr/bin/python3
"""Defines a function that gathers progress data from an API"""
import csv
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


def export_employee_todos(id):
    """Records an employee's tasks in a csv file"""
    # Get the employees id and username
    r = requests.get(f'https://jsonplaceholder.typicode.com/users?id={id}')
    user_id = r.json()[0].get('id')
    user_name = r.json()[0].get('username')

    # Get the employee's todos
    r = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    todos = r.json()

    file_name = f'{id}.csv'

    # Write an employees todos to a csv file
    with open(file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)

        # Go through all the todos of the employee
        for todo in todos:
            todo_status = todo.get('completed')
            todo_title = todo.get('title')
            # Create a todo row and write it the file
            row = [user_id, user_name, todo_status, todo_title]
            writer.writerow(row)


if __name__ == '__main__':
    id = int(sys.argv[1])
    export_employee_todos(id)
