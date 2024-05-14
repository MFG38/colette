import os

todo = []
#todoFile = open('colette_todo', 'r+')

class TodoItem:
    def __init__(self, desc, task_type, deadline):
        self.desc = desc
        self.task_type = task_type
        self.deadline = deadline

    def __str__(self):
        return f"{self.desc} | {self.task_type} | {self.deadline}"
