'''
    main.py

    The main CLI loop.
'''

from commandHandler import CommandHandler as ch
from todoHandler import *
from textColors import *
from dueDateUpdater import *
from reminder import *
from misc import *
from configHandler import *

get_todo_list()
read_todo_list()
get_config_file()
read_config_file()
update_deadlines()
save_todo_list()

if get_config_file() and get_option('start_in_debug_mode') == True:
    ch.toggle_debug_mode()
if get_config_file() and get_option('start_in_test_mode') == True:
    ch.toggle_test_mode()
if get_config_file() and get_option('autoremove_old_entries') == True:
    ch.remove_completed_and_expired_entries()
if not get_config_file() or (get_config_file() and (get_option('enable_reminders') is None or get_option('enable_reminders') == True)):
    print_reminders()

while True:
    cmd = input("cmd> ").split(" ")

    match cmd[0].lower():
        case "help":
            ch.print_help()

        case "ver" | "version":
            ch.print_version_info()

        case "debug":
            ch.toggle_debug_mode()

        case "test":
            ch.toggle_test_mode()

        case "list":
            ch.print_list()

        case "sort":
            ch.sort_list(
                input(f"{TextColor.PROMPT}Sort by desc(ription), type, deadline or status? {TextColor.RESET}"),
                True if input(f"{TextColor.PROMPT}Sort in descending order? [y(es)/N(O)] {TextColor.RESET}") in cmd_yes else False
            )

        case "search":
            ch.search_list(input(f"{TextColor.PROMPT}Enter search term(s): {TextColor.RESET}"))

        case "add":
            t = TodoItem(
                input(f"{TextColor.PROMPT}Description of the task: {TextColor.RESET}"),
                input(f"{TextColor.PROMPT}Type of task ([f]ixed, [d]aily, [w]eekly, [m]onthly): {TextColor.RESET}"),
                input(f"{TextColor.PROMPT}Deadline for the task: {TextColor.RESET}"),
                0
            )
            ch.add_entry(t.desc, t.task_type, t.deadline)

        case "complete" | "done":
            ch.mark_task_as_completed(int(input(f"{TextColor.PROMPT}Index of entry to mark as completed: {TextColor.RESET}")))

        case "rem" | "remove":
            i = input(f"{TextColor.PROMPT}Index or description of entry to remove: {TextColor.RESET}")
            try:
                i = int(i)
                ch.remove_entry_by_index(i)
            except (ValueError, Exception):
                ch.remove_entry_by_description(i)

        case "autorem" | "autoremove" | "arem" | "aremove":
            ch.remove_completed_and_expired_entries()

        case "edit":
            ch.edit_entry(int(input(f"{TextColor.PROMPT}Index of entry to edit: {TextColor.RESET}")))

        case "clear":
            ch.clear_list()

        case "exit" | "quit":
            ch.exit_colette()

        case _:
            print(f"{TextColor.ERROR}{cmd[0]} is not a recognized command.{TextColor.RESET}")
