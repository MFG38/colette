'''
    dueDateUpdater.py

    Handles updating the due dates periodically for tasks
    of a non-fixed type.
'''

import datetime as dt
import calendar

import todoHandler as th

def parse_date_from_string(deadline: str):
    y, m, d = map(int, deadline.split("-"))
    return dt.date(y, m, d)

def add_month(date: dt.date, target_day: int) -> dt.date:
    year = date.year
    month = date.month + 1

    if month > 12:
        month = 1
        year += 1

    last_day = calendar.monthrange(year, month)[1]

    return dt.date(year, month, min(target_day, last_day))

def update_deadlines():
    today = dt.date.today()

    for entry in th.todo:
        due_date, old_due_date = parse_date_from_string(entry.deadline)

        if entry.task_type == 1:
            while due_date < today:
                due_date += dt.timedelta(days=1)
        elif entry.task_type == 2:
            while due_date < today:
                due_date += dt.timedelta(days=7)
        elif entry.task_type == 3:
            target = due_date.day

            while due_date < today:
                due_date = add_month(due_date, target)

        if due_date > old_due_date and entry.task_type != 0:
            entry.status = 0

        entry.deadline = due_date

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
