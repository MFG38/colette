'''
    commandHandler.py

    Defines all of the functions used by the commands in
    Colette's CLI.
'''

import os
import re
#import argparse

import todoHandler as th
from version import *

class CommandHandler:
    def __init__(self, cmd: str):
        self.cmd = cmd

    def print_list():
        '''
        Prints the todo list.
        '''
        header_titles = ["INDEX", "TASK DESCRIPTION", "TYPE", "DUE DATE"]
        justifiers = [7, 63, 7, 15]
        header_length = sum(justifiers)

        if len(th.todo) == 0:
            print("There's nothing in your todo list yet!\nStart by adding something with the ADD command.\n")
        else:
            print(f"{' '.join(str(h.ljust(justifiers[header_titles.index(h)])) for h in header_titles)}")
            print("-" * header_length)

            for entry in th.todo:
                parsed_type = ""

                match entry.task_type:
                    case 0:
                        parsed_type = "fixed"
                    case 1:
                        parsed_type = "daily"
                    case 2:
                        parsed_type = "weekly"
                    case 3:
                        parsed_type = "monthly"
                    case _:
                        parsed_type = "unknown"

                print(
                    str(th.todo.index(entry)).ljust(justifiers[0]),
                    entry.desc.ljust(justifiers[1]),
                    parsed_type.ljust(justifiers[2]),
                    entry.deadline,
                    sep=" "
                )

            print()

    def search_list(search_key: str):
        '''
        Searches the todo list for entries with the given description
        and prints all found entries. Multiple descriptions can be
        given by separating them with commas.
        '''
        pass

    def sort_list(sort_key: str):
        pass

    def add_entry(desc: str, task_type: int, deadline: str):
        '''
        Launches an interactive prompt to add an entry to the
        todo list. The prompt will first ask for a description
        of the task, then a type, and finally its due date.

        The description can be anything as long as it fits within
        60 characters and does not contain a comma anywhere
        within it.

        The type can be one of the following: fixed, daily, weekly,
        monthly. You can also enter only the initial of each type.
        Internally, the type string will be parsed into an integer
        as described:
            0 = fixed
            1 = daily
            2 = weekly
            3 = monthly

        The due date can be provided as one of the following:
            - A full date in YYYY-MM-DD format (ex: 2024-12-31)
            - A month and day in MM-DD format (ex: 12-31)
            - A weekday either typed in full or abbreviated to its
              first 3 letters (ex: Tuesday, Sat)
            - "today" or "tomorrow"
        The due date will be parsed based on its format and converted
        into a usable date internally. For non-fixed due dates, they
        will get automatically updated upon launching Colette if the
        previous due date has passed.
        '''
        if desc == "":
            print("Description can't be an empty string!\nExiting prompt...")
            return
        elif len(desc) > 60:
            print("Length of description exceeds character limit!\nExiting prompt...")
            return

        parsable_type = str(task_type)

        if parsable_type == "fixed" or parsable_type == "f":
            task_type = 0
        elif parsable_type == "daily" or parsable_type == "d":
            task_type = 1
        elif parsable_type == "weekly" or parsable_type == "w":
            task_type = 2
        elif parsable_type == "monthly" or parsable_type == "m":
            task_type = 3
        else:
            print(f"{parsable_type} is not a recognized type!\nExiting prompt...")
            return

        if deadline == "":
            print("Deadline can't be an empty string!\nExiting prompt...")
            return

        item = th.TodoItem(desc, task_type, deadline)
        th.todo.append(item)

    def remove_entry_by_index(index: int):
        '''
        Removes an entry from the todo list by its index.
        '''
        if index not in range(0, len(th.todo)):
            print(f"Nothing found at index {index} - probably out of bounds.\nExiting prompt...")
            return
        else:
            th.todo.remove(th.todo[index])

    def remove_entry_by_description(desc: str):
        '''
        Removes an entry from the todo list by its description.
        Multiple descriptions can be given by separating them with
        commas. If the search returns multiple entries, the program
        will prompt you for the index of the entry to be removed.
        If you wish to remove multiple entries, type them into the
        prompt with their indexes separated by commas.
        '''
        pass

    def remove_expired_entries():
        '''
        Removes all fixed-deadline entries with expired due dates
        from the todo list.
        '''
        pass

    def edit_entry(index: int):
        '''
        Edits an entry in the todo list by its index. An interactive
        prompt will be launched where you will first be prompted for
        the index of the entry you wish to edit. You can then edit
        the description, type and due date of the entry. Specific
        parts of the editing prompt can be skipped by simply pressing
        Enter without typing anything - in this case, that part of
        the entry will be left unmodified.
        '''
        if index not in range(0, len(th.todo)):
            print(f"Nothing found at index {index} - probably out of bounds.\nExiting prompt...")
            return

        new_desc = input("Enter new description or leave blank to skip. ")

        if new_desc == "":
            pass
        else:
            th.todo[index].desc = new_desc

        new_type = input("Enter new type or leave blank to skip. ")

        if new_type == "":
            pass
        elif new_type == "fixed" or new_type == "f":
            th.todo[index].task_type = 0
        elif new_type == "daily" or new_type == "d":
            th.todo[index].task_type = 1
        elif new_type == "weekly" or new_type == "w":
            th.todo[index].task_type = 2
        elif new_type == "monthly" or new_type == "m":
            th.todo[index].task_type = 3
        else:
            print(f"{new_type} is not a recognized type!\nExiting prompt...")
            return

        new_deadline = input("Enter new deadline or leave blank to skip. ")

        if new_deadline == "":
            pass
        else:
            th.todo[index].deadline = new_deadline

    def print_help():
        '''
        Prints this help.
        '''
        print("""
        Colette is a todo list manager that runs in the command line.

        Colette accepts the following commands:
            list - Prints the todo list.

            add - Adds an entry to the todo list.

            rem[ove] - Removes an entry from the todo list by its index.

            edit - Modifies an entry in the todo list.

            help - Prints this help.

            ver[sion] - Prints Colette's version information.

            exit - Saves changes to the todo list and quits Colette.
        """)

    def print_version_info():
        '''
        Prints Colette's version information.
        '''
        print(full_version_info)

    def exit_colette():
        '''
        Saves changes to the todo list and quits Colette.
        '''
        th.save_todo_list()
        exit()
