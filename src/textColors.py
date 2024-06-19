'''
    textColors.py

    Defines text colors for Colette's terminal.
'''

from configHandler import *

get_config_file()
read_config_file()

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

    NULL        = ""
    THEADER     = eval(f"{get_option('table_header_color')}") if get_config_file() and get_option('table_header_color') is not None else NULL
    ERROR       = eval(f"{get_option('error_msg_color')}") if get_config_file() and get_option('error_msg_color') is not None else RED
    WARNING     = eval(f"{get_option('warning_msg_color')}") if get_config_file() and get_option('warning_msg_color') is not None else YELLOW
    DEBUG       = eval(f"{get_option('debug_msg_color')}") if get_config_file() and get_option('debug_msg_color') is not None else CYAN
    PROMPT      = eval(f"{get_option('prompt_msg_color')}") if get_config_file() and get_option('prompt_msg_color') is not None else GREEN
    COMPLETED   = eval(f"{get_option('task_completed_color')}") if get_config_file() and get_option('task_completed_color') is not None else GREEN
    DUESOON     = eval(f"{get_option('task_due_soon_color')}") if get_config_file() and get_option('task_due_soon_color') is not None else BLACK + REDB
    EXPIRED     = eval(f"{get_option('task_expired_color')}") if get_config_file() and get_option('task_expired_color') is not None else BLACK + PURPLEB
    REMINDER    = eval(f"{get_option('reminder_msg_color')}") if get_config_file() and get_option('reminder_msg_color') is not None else YELLOW

if __name__ == "__main__":
    print("Colors ok")
