import os
import re
import datetime
#import argparse
import todoHandler as th

class CommandHandler:
    def __init__(self, cmd: str):
        self.cmd = cmd

    # print_list:
    #   Print the todo list. Possibly add optional arguments for printing
    #   the list sorted by alphabetical order, deadline etc. or filtered by
    #   task type or deadline.
    def print_list():
        if len(th.todo) == 0:
            print("There's nothing in your todo list yet!\nStart by adding something with the ADD command.\n")
        else:
            for entry in th.todo:
                print(str(th.todo.index(entry)), entry.desc, entry.task_type, entry.deadline, sep=" ")

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

        parsable_type = input("Enter a type for the task ([f]ixed, [d]aily, [w]eekly, [m]onthly): ")

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
        #i = int(input("Index of item to remove: "))

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
        pass

    def print_help():
        print("""
        Colette is a todo list manager that runs in the command line.

        Colette accepts the following commands:
            list - Prints the todo list.

            add - Adds an entry to the todo list.

            rem[ove] - Removes an entry from the todo list by its index.

            exit - Quits Colette.
        """)

    # exit_colette:
    #   Self-explanatory.
    def exit_colette():
        exit()
