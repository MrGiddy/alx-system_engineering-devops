#!/usr/bin/python3
"""Defines a function that gathers progress data from an API"""
import requests


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


if __name__ == '__main__':
    import sys

    id = int(sys.argv[1])
    display_todo_progress(id)
