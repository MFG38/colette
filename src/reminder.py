'''
    reminder.py

    Handles printing reminder messages for tasks with
    approaching due dates.
'''

import todoHandler as th
import dateParser as dtp
from textColors import *
from dueDateUpdater import *
# Worth noting about the dueDateUpdater import: parse_date_from_string() is
# only used for testing purposes within this module itself.

def print_reminders():
    remindable_tasks = []

    for entry in th.todo:
        if entry.deadline == dtp.get_current_full_date():
            remindable_tasks.append(entry.desc)

    if len(remindable_tasks) > 0:
        print(f"{TextColor.REMINDER}REMINDER: You have {len(remindable_tasks)} task(s) due today:{TextColor.RESET}")
        for i in remindable_tasks:
            print(i, sep=", ")
        print()

if __name__ == "__main__":
    th.get_todo_list()
    th.read_todo_list()

    for entry in th.todo:
        entry.deadline = parse_date_from_string(entry.deadline)

    print_reminders()
