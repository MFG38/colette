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
    tasks_due_today = []
    tasks_with_passed_deadlines = []

    for entry in th.todo:
        if entry.deadline == dtp.get_current_full_date():
            tasks_due_today.append(entry.desc)
        elif entry.deadline < dtp.get_current_full_date():
            tasks_with_passed_deadlines.append(entry.desc)

    if len(tasks_due_today) > 0:
        print(f"{TextColor.REMINDER}REMINDER: You have {len(tasks_due_today)} task(s) due today:{TextColor.RESET}")
        for i in tasks_due_today:
            print(i, sep=", ")
        print()

    if len(tasks_with_passed_deadlines) > 0:
        print(f"{TextColor.REMINDER}{len(tasks_with_passed_deadlines)} task(s) found with passed due date(s):{TextColor.RESET}")
        for i in tasks_with_passed_deadlines:
            print(i, sep=", ")
        print()

if __name__ == "__main__":
    th.get_todo_list()
    th.read_todo_list()

    for entry in th.todo:
        entry.deadline = parse_date_from_string(entry.deadline)

    print_reminders()
