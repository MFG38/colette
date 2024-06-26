'''
    dateParser.py

    Handles parsing the date from the user's input in case
    they give something like "tomorrow" or a weekday as the
    input and converting it into a usable date. Mostly used
    by the ADD and EDIT commands.
'''

import datetime as dt
import re

from textColors import *

class RegexDates:
    regex_full_date = re.compile(r"\d{4}([-]\d{2}){2}")
    regex_month_day = re.compile(r"\d{2}[-]\d{2}")
    regex_weekday = re.compile(r"mon(day?)?|tue(sday?)?|wed(nesday?)?|thu(rsday?)?|fri(day?)?|sat(urday?)?|sun(day?)?", re.I)
    regex_next_weekday = re.compile(r"^\bnext\b (mon(day?)?|tue(sday?)?|wed(nesday?)?|thu(rsday?)?|fri(day?)?|sat(urday?)?|sun(day?)?)", re.I)

def get_current_full_date():
    return dt.date.today()

def get_current_year():
    return dt.datetime.now().year

def get_current_month():
    return dt.datetime.now().month

def get_current_day():
    return dt.datetime.now().day

def get_current_weekday():
    return dt.datetime.weekday(dt.date.today())

def parse_weekday_from_string(weekday: str):
    parsed_wd = 0

    match weekday.lower():
        case "today":
            parsed_wd = get_current_weekday()
        case "tomorrow":
            parsed_wd = (get_current_weekday() + 1) % 7
        case "mon" | "monday":
            parsed_wd = 0
        case "tue" | "tuesday":
            parsed_wd = 1
        case "wed" | "wednesday":
            parsed_wd = 2
        case "thu" | "thursday":
            parsed_wd = 3
        case "fri" | "friday":
            parsed_wd = 4
        case "sat" | "saturday":
            parsed_wd = 5
        case "sun" | "sunday":
            parsed_wd = 6
        case _:
            pass

    return parsed_wd

def parse_deadline_from_string(deadline: str):
    y, m, d = 1970, 1, 1
    tdelta = 0

    if re.match(RegexDates.regex_full_date, deadline):
        y, m, d = map(int, deadline.split("-"))
    elif re.match(RegexDates.regex_month_day, deadline):
        m, d = map(int, deadline.split("-"))
        if dt.date(get_current_year(), m, d) < get_current_full_date():
            y = (get_current_year() + 1)
        else:
            y = get_current_year()
    elif re.match(RegexDates.regex_weekday, deadline):
        y = get_current_year()
        m = get_current_month()
        d = get_current_day()
        if parse_weekday_from_string(deadline) <= get_current_weekday():
            tdelta = ((parse_weekday_from_string(deadline) - get_current_weekday()) + 7)
        else:
            tdelta = (parse_weekday_from_string(deadline) - get_current_weekday())
    elif re.match(RegexDates.regex_next_weekday, deadline):
        y = get_current_year()
        m = get_current_month()
        d = get_current_day()
        tdelta = ((parse_weekday_from_string(deadline.split(" ").pop(1)) - get_current_weekday()) + 7)
    elif deadline == "today":
        y = get_current_year()
        m = get_current_month()
        d = get_current_day()
    elif deadline == "tomorrow":
        tdelta = 1
        y = get_current_year()
        m = get_current_month()
        d = get_current_day()
    else:
        print(f"{TextColor.ERROR}Failed to parse date from string {deadline}: invalid format.{TextColor.RESET}")

    return (dt.date(y, m, d) + dt.timedelta(days=tdelta))

if __name__ == "__main__":
    print(f"{get_current_full_date()}, {get_current_weekday()}")

    while True:
        p = parse_deadline_from_string(input("test> "))
        print(p)
