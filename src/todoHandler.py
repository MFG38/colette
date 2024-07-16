'''
    todoHandler.py

    Handles stuff related to entries in the todo list in
    Colette. The biggest thing here is the TodoItem class,
    which stores the information needed by each entry. Also
    handles writing the todo list to a file and reading it
    from the generated file.
'''

import os
from textColors import *

tdf_name = 'todo.clt'
todo = []

class TodoItem:
    def __init__(self, desc, task_type, deadline, status):
        self.desc = desc
        self.task_type = task_type
        self.deadline = deadline
        self.status = status

    def __getitem__(self, desc, task_type, deadline, status):
        return self.desc, self.task_type, self.deadline, self.status

def get_todo_list():
    if os.path.exists(tdf_name):
        pass
    else:
        open(tdf_name, 'x')

def read_todo_list():
    with open(tdf_name, 'r') as tdf:
        for line in tdf:
            attribs = line.strip().split(",")
            parsed_entry = TodoItem(str(attribs[0]), int(attribs[1]), str(attribs[2]), int(attribs[3]))
            todo.append(parsed_entry)

def save_todo_list():
    with open(tdf_name, 'w') as tdf:
        for entry in todo:
            tdf.write("{},{},{},{}\n".format(entry.desc, entry.task_type, entry.deadline, entry.status))

def parse_task_type(task_type: int):
    parsed_type = ""

    match task_type:
        case 0:
            parsed_type = "fixed"
        case 1:
            parsed_type = "daily"
        case 2:
            parsed_type = "weekly"
        case 3:
            parsed_type = "monthly"
        case _:
            parsed_type = f"{TextColor.ERROR}unknown{TextColor.RESET}"

    return parsed_type

if __name__ == "__main__":
    get_todo_list()
    read_todo_list()
    for entry in todo:
        print(
            str(todo.index(entry)),
            entry.desc,
            parse_task_type(entry.task_type),
            entry.deadline,
            entry.status,
            sep=", "
        )
