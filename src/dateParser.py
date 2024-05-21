'''
    dateParser.py

    Handles parsing the date from the user's input in case
    they give something like "tomorrow" or a weekday as the
    input and converting it into a usable date. Mostly to
    be used by the ADD and EDIT commands.
'''

import datetime
import calendar
import re

regex_full_date = re.compile(r"\d{4}(.\d{2}){2}")
regex_month_day = re.compile(r"\d{2}.\d{2}")
regex_weekday = re.compile(r"mon(day?)?|tue(sday?)?|wed(nesday?)?|thu(rsday?)?|fri(day?)?|sat(urday?)?|sun(day?)?", re.I)

calendar.setfirstweekday(calendar.MONDAY)

def parse_weekday_from_string(weekday: str):
    parsed_wd = 0

    match weekday.lower():
        case "today":
            parsed_wd = datetime.weekday()
        case "tomorrow":
            parsed_wd = (datetime.weekday() + 1) % 7
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
    pass

def convert_string_to_date(deadline: str):
    pass

if __name__ == "__main__":
    print(datetime.date.today())

    while True:
        p = parse_weekday_from_string(input())
        print(p)
