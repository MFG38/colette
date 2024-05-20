'''
    main.py

    The main CLI loop.
'''

from commandHandler import CommandHandler as ch
from todoHandler import *

while True:
    cmd = input("cmd> ").split(" ")
    cmd_main = cmd[0].lower()
    if len(cmd) > 1:
        cmd_args = cmd[1].lower()

    match cmd_main:
        case "help":
            ch.print_help()

        case "ver" | "version":
            ch.print_version_info()

        case "list":
            ch.print_list()

        case "add":
            t = TodoItem(
                input("Description of the task: "),
                input("Type of task ([f]ixed, [d]aily, [w]eekly, [m]onthly): "),
                input("Deadline for the task: ")
            )
            ch.add_entry(t.desc, t.task_type, t.deadline)

        case "rem" | "remove":
            ch.remove_entry_by_index(int(input("Index of entry to remove: ")))

        case "edit":
            ch.edit_entry(int(input("Index of entry to edit: ")))

        case "exit":
            ch.exit_colette()

        case _:
            print(f"{cmd} is not a recognized command.")
