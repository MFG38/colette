'''
    reminder.py

    Handles printing reminder messages for tasks with
    approaching due dates.
'''

from datetime import timedelta

import todoHandler as th
import dateParser as dtp
from configHandler import *
from textColors import *
from dueDateUpdater import *

def get_reminder_threshold():
    return 1 if not get_config_file() or \
    (get_config_file() and (get_option('reminder_threshold') is None or get_option('reminder_threshold') == 1)) \
    else int(get_option('reminder_threshold'))

def print_reminders():
    tasks_due_today = []
    tasks_due_soon = []
    tasks_with_passed_deadlines = []

    for entry in th.todo:
        if parse_date_from_string(str(entry.deadline)) == dtp.get_current_full_date():
            tasks_due_today.append(entry.desc)
        elif parse_date_from_string(str(entry.deadline)) <= (dtp.get_current_full_date() + timedelta(days=get_reminder_threshold())) \
        and parse_date_from_string(str(entry.deadline)) > dtp.get_current_full_date():
            tasks_due_soon.append(entry.desc)
        elif parse_date_from_string(str(entry.deadline)) < dtp.get_current_full_date():
            tasks_with_passed_deadlines.append(entry.desc)

    if len(tasks_due_today) > 0:
        print(f"{TextColor.REMINDER}REMINDER: You have {len(tasks_due_today)} task(s) due today:{TextColor.RESET}")
        for i in tasks_due_today:
            print(i, sep=", ")
        print()
    if len(tasks_due_soon) > 0:
        print(f"{TextColor.REMINDER}REMINDER: You have {len(tasks_due_soon)} task(s) due in {get_reminder_threshold()} day(s):{TextColor.RESET}")
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
