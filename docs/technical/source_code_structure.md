# Source code structure

---

This page contains information about the files contained in Colette's source code.

## Source files

Below is a list of the files in the **src/** directory and the variables, classes and functions defined within them.

### commandHandler.py

Defines all of the functions used by the commands in Colette's CLI.

```text
def         print_formatted_entries
class       CommandHandler
    def     print_list
    def     search_list
    def     sort_list
    def     clear_list
    def     add_entry
    def     mark_task_as_completed
    def     remove_entry_by_index
    def     remove_entry_by_description
    def     remove_completed_and_expired_entries
    def     edit_entry
    def     print_help
    def     print_version_info
    def     exit_colette
    def     toggle_debug_mode
    def     toggle_test_mode
```

### configHandler.py

Handles reading information from a configuration file if one is found in the working directory or `~/.config/` on launch.

```text
var         conf_path
var         conf_name
def         get_config_file
def         read_config_file
def         get_option
```

### dateParser.py

Handles parsing the date from the user's input in case they give something like "tomorrow" or a weekday as the input and converting it into a usable date. Mostly used by the **[add](../cmd/add.md)** and **[edit](../cmd/edit.md)** commands.

```text
class       RegexDates
    var     regex_full_date
    var     regex_month_day
    var     regex_weekday
    var     regex_next_weekday
def         get_current_full_date
def         get_current_year
def         get_current_month
def         get_current_day
def         get_current_weekday
def         parse_weekday_from_string
def         parse_deadline_from_string
```

### dueDateUpdater.py

Handles updating the due dates periodically for tasks of a non-fixed type. The `parse_date_from_string()` function is also contained here.

```text
def         parse_date_from_string
def         update_deadlines
```

### main.py

The main CLI loop.

This module does not contain any variable, class or function definitions.

### misc.py

Miscellaneous variables etc. used by some functions.

```text
var         header_titles
var         justifiers
var         header_length
var         cmd_yes
var         cmd_no
```

### reminder.py

Handles printing reminder messages for tasks with approaching due dates.

```text
def         get_reminder_threshold
def         print_reminders
```

### settings.py

Stores various settings used by Colette.

```text
var         debug_mode
var         test_mode
```

### textColors.py

Defines text colors for Colette's terminal.

```text
class       TextColor
    var     BLACK
    var     RED
    var     GREEN
    var     YELLOW
    var     BLUE
    var     PURPLE
    var     CYAN
    var     WHITE
    var     BLACKB
    var     REDB
    var     GREENB
    var     YELLOWB
    var     BLUEB
    var     PURPLEB
    var     CYANB
    var     WHITEB
    var     RESET
    var     NULL
    var     THEADER
    var     ERROR
    var     WARNING
    var     DEBUG
    var     PROMPT
    var     COMPLETED
    var     DUESOON
    var     EXPIRED
    var     REMINDER
```

### todoHandler.py

Handles stuff related to entries in the todo list in Colette. The biggest thing here is the `TodoItem` class, which stores the information needed by each entry. Also handles writing the todo list to a file and reading it from the generated file.

```text
class       TodoItem
def         get_todo_list
def         read_todo_list
def         save_todo_list
def         parse_task_type
```

### version.py

Stores Colette's version information.

```text
var         version_num
var         version_date
var         full_version_info
```

## Other files and directories

### docs/

The source files for Colette's documentation are contained in this directory.

### .editorconfig

Colette's editorconfig file used for formatting the code across different files. Some text editors support .editorconfig out of the box; if yours does not, please install an extension that adds .editorconfig support before writing any code.

### .gitattributes and .gitignore

Colette's Git configuration files.

### build.sh

Shell script used for building Colette and its documentation. Invokes `pyinstaller` and `mkdocs` internally.

### CHANGELOG.md

Colette's changelog.

### clean-cache.sh

Shell script used for cleaning and deleting \_\_pycache\_\_ if it is found in the **src/** directory.

### clean-genfiles.sh

Shell script used for deleting todo.clt and colette.toml if they are found in the root directory.

### LICENSE

Text file containing Colette's license information.

### mkdocs.yml

Configuration file used by mkdocs for generating the HTML for the documentation.

### pack-dist.sh

Shell script used for packaging a distributable .zip file with a pre-compiled executable and the documentation of Colette.

### README.md

The readme file.

### requirements.txt

Text file containing the names of the `pip` packages that Colette needs for its build workflow. Install them with `pip install -r requirements.txt` before building Colette.

### update-docs-changelog.sh

Shell script used for making a copy of CHANGELOG.md in the **docs/** directory. build.sh also calls this script in the documentation build stage before invoking `mkdocs`.

### VERSION

Text file containing Colette's version number. pack-dist.sh reads the information from this file into a variable and uses it to package Colette with the proper version number.
