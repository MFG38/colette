'''
    dateParser.py

    Handles parsing the date from the user's input in case
    they give something like "tomorrow" or a weekday as the
    input and converting it into a usable date. Mostly to
    be used by the ADD and EDIT commands.
'''

import datetime as dt
import calendar
import re

class RegexDates:
    regex_full_date = re.compile(r"\d{4}(.\d{2}){2}")
    regex_month_day = re.compile(r"\d{2}.\d{2}")
    regex_weekday = re.compile(r"mon(day?)?|tue(sday?)?|wed(nesday?)?|thu(rsday?)?|fri(day?)?|sat(urday?)?|sun(day?)?", re.I)

#calendar.setfirstweekday(calendar.MONDAY)

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

    match deadline:
        case RegexDates.regex_full_date:
            y = deadline[0:3]
            m = deadline[5:6]
            d = deadline[8:9]
        case RegexDates.regex_month_day:
            y = get_current_year()
            m = deadline[5:6]
            d = deadline[8:9]
        case RegexDates.regex_weekday:
            y = get_current_year()
            m = get_current_month()
            d = (get_current_day() + parse_weekday_from_string(deadline))
        case "today":
            y = get_current_year()
            m = get_current_month()
            d = get_current_day()
        case "tomorrow":
            y = get_current_year()
            m = get_current_month()
            d = (get_current_day() + 1)
        case _:
            print(f"Failed to parse date from string {deadline}: invalid format.")

    return dt.date(y, m, d)

def convert_string_to_date(deadline: str):
    pass

if __name__ == "__main__":
    print(f"{dt.date.today()}, {get_current_weekday()}")

    while True:
        p = parse_weekday_from_string(input("test> "))
        print(p)
