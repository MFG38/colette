'''
    todoHandler.py

    Handles stuff related to entries in the todo list in
    Colette. The biggest thing here is the TodoItem class,
    which stores the information needed by each entry. Also
    handles writing the todo list to a file and reading it
    from the generated file.
'''

import os

tdf_name = 'todo.clt'
todo = []

class TodoItem:
    def __init__(self, desc, task_type, deadline):
        self.desc = desc
        self.task_type = task_type
        self.deadline = deadline

    def __getitem__(self, desc, task_type, deadline):
        return self.desc, self.task_type, self.deadline

def get_todo_list():
    if os.path.exists(tdf_name):
        pass
    else:
        open(tdf_name, 'x')

def read_todo_list():
    with open(tdf_name, 'r') as tdf:
        for line in tdf:
            attribs = line.strip().split(",")
            parsed_entry = TodoItem(str(attribs[0]), int(attribs[1]), str(attribs[2]))
            todo.append(parsed_entry)

def save_todo_list():
    wd = os.getcwd()

    with open(tdf_name, 'w') as tdf:
        for entry in todo:
            tdf.write("{},{},{}\n".format(entry.desc, entry.task_type, entry.deadline))

    #print(f"{tdf_name} saved in {wd}")

if __name__ == "__main__":
    get_todo_list()
    read_todo_list()
    for entry in todo:
        print(
            str(todo.index(entry)),
            entry.desc,
            entry.task_type,
            entry.deadline,
            sep=", "
        )
