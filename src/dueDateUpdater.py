'''
    dueDateUpdater.py

    Handles updating the due dates periodically for tasks
    of a non-fixed type.
'''

import datetime as dt
import calendar

import todoHandler as th
import dateParser as dtp

def parse_date_from_string(deadline: str):
    y, m, d = map(int, deadline.split("-"))
    return dt.date(y, m, d)

def update_deadlines():
    for entry in th.todo:
        y, m, d = map(int, entry.deadline.split("-"))
        tdelta = 0

        if entry.task_type == 1 and parse_date_from_string(entry.deadline) < dt.date.today():
            tdelta = 1
            if entry.status > 0:
                entry.status = 0
        elif entry.task_type == 2 and parse_date_from_string(entry.deadline) < dt.date.today():
            tdelta = 7
            if entry.status > 0:
                entry.status = 0
        elif entry.task_type == 3 and parse_date_from_string(entry.deadline) < dt.date.today():
            tdelta = calendar.monthrange(dtp.get_current_year(), dtp.get_current_month())
            if entry.status > 0:
                entry.status = 0

        entry.deadline = (dt.date(y, m, d) + dt.timedelta(days=tdelta))

if __name__ == "__main__":
    th.get_todo_list()
    th.read_todo_list()
    update_deadlines()

    for entry in th.todo:
        print(
            str(th.todo.index(entry)),
            entry.desc,
            entry.task_type,
            entry.deadline,
            sep=", "
        )
