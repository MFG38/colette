'''
    main.py

    The main CLI loop.
'''

from commandHandler import CommandHandler as ch
from todoHandler import *
from textColors import *

get_todo_list()
read_todo_list()

while True:
    cmd = input("cmd> ").split(" ")
    cmd_main = cmd[0].lower()
    if len(cmd) > 1:
        cmd_args = cmd[1:].lower()

    match cmd_main:
        case "help":
            ch.print_help()

        case "ver" | "version":
            ch.print_version_info()

        case "list":
            ch.print_list()

        case "search":
            ch.search_list(input(f"{TextColor.PROMPT}Enter search term(s): {TextColor.RESET}"))

        case "add":
            t = TodoItem(
                input(f"{TextColor.PROMPT}Description of the task: {TextColor.RESET}"),
                input(f"{TextColor.PROMPT}Type of task ([f]ixed, [d]aily, [w]eekly, [m]onthly): {TextColor.RESET}"),
                input(f"{TextColor.PROMPT}Deadline for the task: {TextColor.RESET}")
            )
            ch.add_entry(t.desc, t.task_type, t.deadline)

        case "rem" | "remove":
            i = int(input(f"{TextColor.PROMPT}Index of entry to remove: {TextColor.RESET}"))
            '''if str(i) == "":
                pass
            elif int(i) >= 0:'''
            ch.remove_entry_by_index(i)

        case "edit":
            i = int(input(f"{TextColor.PROMPT}Index of entry to edit: {TextColor.RESET}"))
            ch.edit_entry(i)

        case "exit":
            ch.exit_colette()

        case _:
            print(f"{TextColor.ERROR}{cmd_main} is not a recognized command.{TextColor.RESET}")
