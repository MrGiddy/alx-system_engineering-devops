#!/usr/bin/python3
"""Defines a function that gathers tasks data from an API"""
import csv
import requests
import sys


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


if __name__ == '__main__':
    id = int(sys.argv[1])
    export_employee_todos_csv(id)
