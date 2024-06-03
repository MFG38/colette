'''
    main.py

    The main CLI loop.
'''

from commandHandler import CommandHandler as ch
from todoHandler import *
from textColors import *
from dueDateUpdater import *
from reminder import *

get_todo_list()
read_todo_list()

update_deadlines()
print_reminders()

while True:
    cmd = input("cmd> ").split(" ")

    match cmd[0]:
        case "help":
            ch.print_help()

        case "ver" | "version":
            ch.print_version_info()

        case "list":
            ch.print_list()

        case "sort":
            ch.sort_list(input(f"{TextColor.PROMPT}Sort by desc(ription), type or deadline? {TextColor.RESET}"))

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
            i = input(f"{TextColor.PROMPT}Index or description of entry to remove: {TextColor.RESET}")
            try:
                i = int(i)
                ch.remove_entry_by_index(i)
            except (ValueError, Exception):
                ch.remove_entry_by_description(i)

        case "autorem" | "autoremove" | "arem" | "aremove":
            ch.remove_expired_entries()

        case "edit":
            ch.edit_entry(int(input(f"{TextColor.PROMPT}Index of entry to edit: {TextColor.RESET}")))

        case "clear":
            ch.clear_list()

        case "exit" | "quit":
            ch.exit_colette()

        case _:
            print(f"{TextColor.ERROR}{cmd_main} is not a recognized command.{TextColor.RESET}")
