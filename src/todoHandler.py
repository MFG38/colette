'''
    todoHandler.py

    Handles stuff related to entries in the todo list in
    Colette. The biggest thing here is the TodoItem class,
    which stores the information needed by each entry.
'''

import os
import datetime

todo = []

class TodoItem:
    def __init__(self, desc, task_type, deadline):
        self.desc = desc
        self.task_type = task_type
        self.deadline = deadline
