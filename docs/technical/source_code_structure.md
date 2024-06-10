# Source code structure

---

## Source files

Below is a list of the files in the **src/** directory and their functionality.

### commandHandler.py

Defines all of the functions used by the commands in Colette's CLI.

### dateParser.py

Handles parsing the date from the user's input in case they give something like "tomorrow" or a weekday as the input and converting it into a usable date. Mostly used by the **[add](../cmd/add.md)** and **[edit](../cmd/edit.md)** commands.

### dueDateUpdater.py

Handles updating the due dates periodically for tasks of a non-fixed type.

### main.py

The main CLI loop.

### misc.py

Miscellaneous variables etc. used by some functions.

### reminder.py

Handles printing reminder messages for tasks with approaching due dates.

### settings.py

Stores various settings used by Colette.

### textColors.py

Defines text colors for Colette's terminal.

### todoHandler.py

Handles stuff related to entries in the todo list in Colette. The biggest thing here is the `TodoItem` class, which stores the information needed by each entry. Also handles writing the todo list to a file and reading it from the generated file.

### version.py

Stores Colette's version information.