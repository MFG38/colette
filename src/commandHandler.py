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

    # print_list:
    #   Print the todo list. Possibly add optional arguments for printing
    #   the list sorted by alphabetical order, deadline etc. or filtered by
    #   task type or deadline.
    def print_list():
        header_titles = ["INDEX", "TASK DESCRIPTION", "TYPE", "DUE DATE"]
        justifiers = [6, 64, 8, 12]
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

    # search_list:
    #   Search the todo list based on a given search key and return all
    #   matching entries.
    def search_list(search_key: str):
        pass

    # sort_list:
    #   Sort the todo list and save the changes to the file. Sortable by
    #   alphabetical order, type or deadline date. Possibly ask the user
    #   if they would like to simply view a sorted version of the list
    #   before doing anything.
    def sort_list(sort_key: str):
        pass

    # add_entry:
    #   Add an entry to the todo list. Ask for a description of the task,
    #   its type (choice between fixed deadline, daily, weekly or monthly)
    #   and a deadline date. Possibility for making the deadline optional or
    #   self-updating depending on type. Possibly add command line parameters
    #   for setting the properties "in advance" to skip parts of the prompt.
    def add_entry(desc: str, task_type: int, deadline: str):
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

        # The deadline date will need some sort of parsing/conversion solution.
        if deadline == "":
            print("Deadline can't be an empty string!\nExiting prompt...")
            return

        item = th.TodoItem(desc, task_type, deadline)
        th.todo.append(item)

    # remove_entry_by_index:
    #   Remove an entry from the list by its index.
    def remove_entry_by_index(index: int):
        if index not in range(0, len(th.todo)):
            print(f"Nothing found at index {index} - probably out of bounds.\nExiting prompt...")
            return
        else:
            th.todo.remove(th.todo[index])

    # remove_entry_by_description:
    #   Remove an entry from the list by (part of) its description. If multiple
    #   entries with the description are found, ask the user which one
    #   to remove.
    def remove_entry_by_description(desc: str):
        pass

    # remove_expired_entries:
    #   Remove all old entries from the list based on a given deadline date.
    #   Probably apply to fixed deadlines only.
    def remove_expired_entries(deadline: str):
        pass

    # edit_entry:
    #   Edit an entry in the todo list. Ask the user for the index of the entry
    #   they wish to edit and launch an interactive editing prompt. Possibly add
    #   optional arguments to edit only part of the entry without an interactive
    #   prompt.
    def edit_entry(index: int):
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

    # print_help:
    #   Self-explanatory.
    def print_help():
        print("""
        Colette is a todo list manager that runs in the command line.

        Colette accepts the following commands:
            list - Prints the todo list.

            add - Adds an entry to the todo list.

            rem[ove] - Removes an entry from the todo list by its index.

            ver[sion] - Prints Colette's version information. Supports the
            following command line arguments:
                -n, --num: Prints only the version number.
                -d, --date: Prints only the version date.

            exit - Quits Colette.
        """)

    # print_version_info:
    #   Self-explanatory. Optional command line arguments for only printing
    #   version number or date, print full version info if no arguments are
    #   passed.
    def print_version_info():
        '''parser = argparse.ArgumentParser()
        argg = parser.add_mutually_exclusive_group()
        argg.add_argument('-n', '--num')
        argg.add_argument('-d', '--date')
        args = parser.parse_args()

        if args.num:
            print(version_num)
        elif args.date:
            print(version_date)
        else:'''
        print(full_version_info)

    # exit_colette:
    #   Self-explanatory.
    def exit_colette():
        exit()
