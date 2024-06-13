'''
    reminder.py

    Handles printing reminder messages for tasks with
    approaching due dates.
'''

from datetime import timedelta

import todoHandler as th
import dateParser as dtp
import configHandler as cnf
from textColors import *
from dueDateUpdater import *

def print_reminders():
    tasks_due_today = []
    tasks_due_tomorrow = []
    tasks_with_passed_deadlines = []

    for entry in th.todo:
        if parse_date_from_string(entry.deadline) == dtp.get_current_full_date():
            tasks_due_today.append(entry.desc)
        elif parse_date_from_string(entry.deadline) == (dtp.get_current_full_date() + timedelta(days=1)):
            tasks_due_tomorrow.append(entry.desc)
        elif parse_date_from_string(entry.deadline) < dtp.get_current_full_date():
            tasks_with_passed_deadlines.append(entry.desc)

    if len(tasks_due_today) > 0 and len(tasks_due_tomorrow) == 0:
        print(f"{TextColor.REMINDER}REMINDER: You have {len(tasks_due_today)} task(s) due today:{TextColor.RESET}")
        for i in tasks_due_today:
            print(i, sep=", ")
        print()
    elif len(tasks_due_tomorrow) > 0 and len(tasks_due_today) == 0:
        print(f"{TextColor.REMINDER}REMINDER: You have {len(tasks_due_tomorrow)} task(s) due tomorrow:{TextColor.RESET}")
        for i in tasks_due_tomorrow:
            print(i, sep=", ")
        print()
    elif len(tasks_due_today) > 0 and len(tasks_due_tomorrow) > 0:
        tasks_due_soon = list(tasks_due_today + tasks_due_tomorrow)
        print(f"{TextColor.REMINDER}REMINDER: You have {len(tasks_due_today)} task(s) due today and {len(tasks_due_tomorrow)} due tomorrow:{TextColor.RESET}")
        for i in tasks_due_soon:
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
