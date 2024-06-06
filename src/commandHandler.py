'''
    commandHandler.py

    Defines all of the functions used by the commands in
    Colette's CLI.
'''

import sys
import re
import argparse
from datetime import date

import todoHandler as th
import dateParser as dtp
import settings
from textColors import *
from version import *
from misc import *

class CommandHandler:
    def __init__(self, cmd: str):
        self.cmd = cmd

    def print_list():
        '''
        Prints the todo list.
        '''
        if len(th.todo) == 0:
            print("There's nothing in your todo list yet!\nStart by adding something with the ADD command.\n")
        else:
            print(f"{''.join(str(h.ljust(justifiers[header_titles.index(h)])) for h in header_titles)}")
            print("-" * header_length)

            for entry in th.todo:
                print(
                    f"{TextColor.DUETODAY}" if entry.deadline == dtp.get_current_full_date() else "",
                    f"{TextColor.EXPIRED}" if entry.deadline < dtp.get_current_full_date() else "",
                    str(th.todo.index(entry)).ljust(justifiers[0]),
                    entry.desc.ljust(justifiers[1]),
                    th.parse_task_type(entry.task_type).ljust(justifiers[2]),
                    entry.deadline,
                    f"{TextColor.RESET}" if entry.deadline <= dtp.get_current_full_date() else "",
                    sep=""
                )

            print()

    def search_list(search_key: str):
        '''
        Searches the todo list for entries with the given description
        and prints all found entries.
        '''
        found_entries = []

        if search_key != "":
            for entry in th.todo:
                if re.search(search_key, entry.desc):
                    found_entries.append(entry)

            if len(found_entries) > 0:
                for entry in found_entries:
                    print(
                        f"{TextColor.DUETODAY}" if entry.deadline == dtp.get_current_full_date() else "",
                        f"{TextColor.EXPIRED}" if entry.deadline < dtp.get_current_full_date() else "",
                        str(th.todo.index(entry)).ljust(justifiers[0]),
                        entry.desc.ljust(justifiers[1]),
                        th.parse_task_type(entry.task_type).ljust(justifiers[2]),
                        entry.deadline,
                        f"{TextColor.RESET}" if entry.deadline <= dtp.get_current_full_date() else "",
                        sep=""
                    )
                print()
            else:
                print(f"No results returned with the search term(s) '{search_key}'.")
                print()

        if settings.debug_mode == True:
            print(f"{TextColor.DEBUG}Search term(s) '{search_key}' returned {len(found_entries)} entries.{TextColor.RESET}")

        return len(found_entries)

    def sort_list(sort_key: str, desc_order: bool):
        '''
        Sorts the todo list by a given key. The key can be either
        desc(ription), type or deadline.
        '''
        if sort_key == "desc" or sort_key == "description":
            th.todo.sort(reverse=desc_order, key=lambda TodoItem: TodoItem.desc)
        elif sort_key == "type":
            th.todo.sort(reverse=desc_order, key=lambda TodoItem: TodoItem.task_type)
        elif sort_key == "deadline":
            th.todo.sort(reverse=desc_order, key=lambda TodoItem: TodoItem.deadline)
        else:
            print(f"{TextColor.ERROR}{sort_key} is not a valid sort key!{TextColor.RESET}")

        if settings.debug_mode == True:
            print(f"{TextColor.DEBUG}Sorting todo list by {sort_key}...{TextColor.RESET}")

        th.save_todo_list()

    def clear_list():
        '''
        Clears the entire todo list. Use with caution!
        '''
        if settings.debug_mode == True:
            print(f"{TextColor.DEBUG}Clearing todo list...{TextColor.RESET}")

        th.todo.clear()
        th.save_todo_list()

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
              first 3 letters, optionally preceded by "next"
              (ex: Tuesday, Sat, next Friday)
            - "today" or "tomorrow"
        The due date will be parsed based on its format and converted
        into a usable date internally. For tasks with non-fixed due
        dates, their due dates will get automatically updated upon
        launching Colette if the previous due date has passed.
        '''
        if desc == "":
            print(f"{TextColor.ERROR}Description can't be an empty string!{TextColor.RESET}")
            return
        elif len(desc) > 60:
            print(f"{TextColor.ERROR}Length of description exceeds character limit!{TextColor.RESET}")
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
            print(f"{TextColor.ERROR}{parsable_type} is not a recognized type!{TextColor.RESET}")
            return

        if deadline == "":
            print(f"{TextColor.ERROR}Deadline can't be an empty string!{TextColor.RESET}")
            return

        item = th.TodoItem(desc, task_type, dtp.parse_deadline_from_string(deadline))
        th.todo.append(item)

        th.save_todo_list()

        if settings.debug_mode == True:
            print(f"{TextColor.DEBUG}Added entry at index {len(th.todo) - 1}.{TextColor.RESET}")

    def remove_entry_by_index(index: int):
        '''
        Removes an entry from the todo list by its index.
        '''
        if index not in range(0, len(th.todo)):
            print(f"{TextColor.ERROR}Nothing found at index {index} - probably out of bounds.{TextColor.RESET}")
            return
        else:
            if settings.debug_mode == True:
                print(f"{TextColor.DEBUG}Removing entry at index {index}...{TextColor.RESET}")
            th.todo.remove(th.todo[index])

        th.save_todo_list()

    def remove_entry_by_description(desc: str):
        '''
        Removes an entry from the todo list by its description.
        If the search returns multiple entries, the program
        will prompt you for the index of the entry to be removed.
        If you wish to remove multiple entries, type them into the
        prompt with their indexes separated by commas.
        '''
        removable_entries = []

        if desc != "":
            for entry in th.todo:
                if re.search(desc, entry.desc):
                    removable_entries.append(entry)

            if len(removable_entries) > 0:
                for entry in removable_entries:
                    print(
                        f"{TextColor.DUETODAY}" if entry.deadline == dtp.get_current_full_date() else "",
                        f"{TextColor.EXPIRED}" if entry.deadline < dtp.get_current_full_date() else "",
                        str(th.todo.index(entry)).ljust(justifiers[0]),
                        entry.desc.ljust(justifiers[1]),
                        th.parse_task_type(entry.task_type).ljust(justifiers[2]),
                        entry.deadline,
                        f"{TextColor.RESET}" if entry.deadline <= dtp.get_current_full_date() else "",
                        sep=""
                    )
                print()

                if len(removable_entries) == 1:
                    choice = input(f"{TextColor.PROMPT}Remove this entry from the todo list? [y(es)/N(O)] {TextColor.RESET}")

                    if choice == "yes" or choice == "y":
                        if settings.debug_mode == True:
                            print(f"{TextColor.DEBUG}Removing entry at index {removable_entries}...{TextColor.RESET}")
                        CommandHandler.remove_entry_by_index(int(th.todo.index(removable_entries[0])))
                    else:
                        pass
                elif len(removable_entries) >= 2:
                    rem_these = input(f"{TextColor.PROMPT}Multiple entries containing '{desc}' were found.\nWhich entry/entries do you wish to remove? {TextColor.RESET}").split(",")
                    rem_these.sort()
                    rem_these.reverse()

                    if len(rem_these) == 0:
                        pass
                    else:
                        for i in rem_these:
                            if settings.debug_mode == True:
                                print(f"{TextColor.DEBUG}Removing entries at indexes {removable_entries}...{TextColor.RESET}")
                            CommandHandler.remove_entry_by_index(int(i))
            else:
                print(f"No results returned with the search term(s) '{desc}'.")
                print()

        th.save_todo_list()

    def remove_expired_entries():
        '''
        Removes all fixed-deadline entries with expired due dates
        from the todo list.
        '''
        for entry in th.todo:
            if entry.task_type == 0 and entry.deadline < date.today():
                th.todo.remove(th.todo[th.todo.index(entry)])

        th.save_todo_list()

        if settings.debug_mode == True:
            print(f"{TextColor.DEBUG}{TextColor.RESET}")

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
            print(f"{TextColor.ERROR}Nothing found at index {index} - probably out of bounds.{TextColor.RESET}")
            return

        new_desc = input(f"{TextColor.PROMPT}Enter new description or leave blank to skip. {TextColor.RESET}")

        if new_desc == "":
            pass
        else:
            th.todo[index].desc = new_desc

        new_type = input(f"{TextColor.PROMPT}Enter new type or leave blank to skip. {TextColor.RESET}")

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
            print(f"{TextColor.ERROR}{new_type} is not a recognized type!{TextColor.RESET}")
            return

        new_deadline = input(f"{TextColor.PROMPT}Enter new deadline or leave blank to skip. {TextColor.RESET}")

        if new_deadline == "":
            pass
        else:
            th.todo[index].deadline = dtp.parse_deadline_from_string(new_deadline)

        th.save_todo_list()

        if settings.debug_mode == True:
            print(f"{TextColor.DEBUG}Edited entry at index {index}.{TextColor.RESET}")

    def print_help():
        '''
        Prints a help message with a description of Colette and a
        list of its commands.
        '''
        print("""
        Colette is a todo list manager that runs in the command line.

        Colette accepts the following commands:
            list - Prints the todo list.

            search - Searches the todo list for entries with the given
            description and prints the results.

            sort - Sorts the todo list by a given key.

            add - Adds an entry to the todo list.

            rem[ove] - Removes an entry from the todo list.

            a[uto]rem[ove] - Removes all fixed-deadline extries with
            expired due dates from the todo list.

            edit - Modifies an entry in the todo list.

            clear - Clears the entire todo list. Use with caution!

            help - Prints this help.

            ver[sion] - Prints Colette's version information.

            debug - Toggles debug mode.

            exit/quit - Quits Colette.
        """)

    def print_version_info():
        '''
        Prints Colette's version information.
        '''
        print(full_version_info)

    def exit_colette():
        '''
        Quits Colette.
        '''
        sys.exit()

    def toggle_debug_mode():
        '''
        Toggles debug mode.
        '''
        settings.debug_mode = not settings.debug_mode
        print(f"{TextColor.DEBUG}Debug mode is now {settings.debug_mode}.{TextColor.RESET}")
