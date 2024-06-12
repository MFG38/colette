'''
    textColors.py

    Defines text colors for Colette's terminal.
'''

from configHandler import *

get_config_file()
read_config_file()

def format_color_string_from_config(key: str):
    color_code = format(f"{get_option(key)}")
    return f"{TextColor.color_code}"

class TextColor:
    BLACK       = "\033[30m"
    RED         = "\033[31m"
    GREEN       = "\033[32m"
    YELLOW      = "\033[33m"
    BLUE        = "\033[34m"
    PURPLE      = "\033[35m"
    CYAN        = "\033[36m"
    WHITE       = "\033[37m"

    BLACKB      = "\033[40m"
    REDB        = "\033[41m"
    GREENB      = "\033[42m"
    YELLOWB     = "\033[43m"
    BLUEB       = "\033[44m"
    PURPLEB     = "\033[45m"
    CYANB       = "\033[46m"
    WHITEB      = "\033[47m"

    RESET       = "\033[0m"

    DEFAULT     = WHITE
    ERROR       = format_color_string_from_config('error_msg_color') if get_option('error_msg_color') is not None else RED
    WARNING     = format_color_string_from_config('warning_msg_color') if get_option('warning_msg_color') is not None else YELLOW
    DEBUG       = format_color_string_from_config('debug_msg_color') if get_option('debug_msg_color') is not None else CYAN
    PROMPT      = format_color_string_from_config('prompt_msg_color') if get_option('prompt_msg_color') is not None else GREEN
    COMPLETED   = format_color_string_from_config('task_completed_color') if get_option('task_completed_color') is not None else GREEN
    DUESOON     = format_color_string_from_config('task_due_soon_color') if get_option('task_due_soon_color') is not None else BLACK + REDB
    EXPIRED     = format_color_string_from_config('task_expired_color') if get_option('task_expired_color') is not None else BLACK + PURPLEB
    REMINDER    = format_color_string_from_config('reminder_msg_color') if get_option('reminder_msg_color') is not None else YELLOW

if __name__ == "__main__":
    print("Colors ok")
