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

def parse_color(value: str) -> str:
    colors = []

    for color in value.split("+"):
        name = color.strip().upper()

        try:
            colors.append(getattr(TextColor, name))
        except AttributeError:
            raise ValueError(f"Unknown text color: {name!r}")

    return "".join(colors)

TextColor.THEADER   = parse_color(get_option('table_header_color')) if get_config_file() and get_option('table_header_color') is not None else TextColor.NULL
TextColor.ERROR     = parse_color(get_option('error_msg_color')) if get_config_file() and get_option('error_msg_color') is not None else TextColor.RED
TextColor.WARNING   = parse_color(get_option('warning_msg_color')) if get_config_file() and get_option('warning_msg_color') is not None else TextColor.YELLOW
TextColor.DEBUG     = parse_color(get_option('debug_msg_color')) if get_config_file() and get_option('debug_msg_color') is not None else TextColor.CYAN
TextColor.PROMPT    = parse_color(get_option('prompt_msg_color')) if get_config_file() and get_option('prompt_msg_color') is not None else TextColor.GREEN
TextColor.COMPLETED = parse_color(get_option('task_completed_color')) if get_config_file() and get_option('task_completed_color') is not None else TextColor.GREEN
TextColor.DUESOON   = parse_color(get_option('task_due_soon_color')) if get_config_file() and get_option('task_due_soon_color') is not None else TextColor.BLACK + TextColor.REDB
TextColor.EXPIRED   = parse_color(get_option('task_expired_color')) if get_config_file() and get_option('task_expired_color') is not None else TextColor.BLACK + TextColor.PURPLEB
TextColor.REMINDER  = parse_color(get_option('reminder_msg_color')) if get_config_file() and get_option('reminder_msg_color') is not None else TextColor.YELLOW

if __name__ == "__main__":
    print(f"{TextColor.THEADER}does this work{TextColor.RESET}")
    print(f"{TextColor.DEBUG}does this work{TextColor.RESET}")
