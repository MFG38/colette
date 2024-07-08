# Colette changelog

---

## v0.2.2 (WIP)

- **Added:** Additional configuration options:
    - `reminder_threshold`: Sets the number of days at/below which Colette will print a reminder about a task with an approaching due date.
- **Fixed:** Tasks with passed due dates being printed under reminders instead of passed due date notifications.
- **Fixed:** `autoremove` command was only removing single entries instead of multiple.

## v0.2.1 (2024-06-26)

- **Added:** Two additional configuration options:
    - `print_header_separator`: Controls printing the separator line between the table header and task list in the output of the `list` command.
    - `table_header_color`: Sets the display color(s) for the table header in the output of the `list` command.

## v0.2.0 (2024-06-18)

- **Added:** Configuration support through a TOML file.
- **Fixed:** Command prompt was not case-insensitive.
- **Fixed:** Possible crashes when attempting string operations on datetime objects.

## v0.1.0 (2024-06-11)

- Initial release.