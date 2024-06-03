'''
    textColors.py

    Defines text colors for Colette's terminal.
'''

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

    # These I'll probably make configurable at some point.
    DEFAULT     = WHITE
    ERROR       = RED
    WARNING     = YELLOW
    DEBUG       = CYAN
    PROMPT      = GREEN
    DUETODAY    = BLACK + REDB
    EXPIRED     = BLACK + PURPLEB
    REMINDER    = YELLOW

if __name__ == "__main__":
    print("Colors ok")
