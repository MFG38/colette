# Configuration

---

Colette is configurable with a TOML file. TOML is a simple, human-readable markup language used by various pieces of software for their configuration, Colette included. See the [TOML website](https://toml.io/en/) for more information and a syntax reference.

Colette does not generate a configuration file by itself; rather, the user can create a configuration file for Colette if they wish to change the default settings. If you wish to configure Colette, create a file named **colette.toml** in the directory where Colette is located and add any settings you wish to modify into that file. See [Available settings](#available-settings) for a list of configuration options.

## Available settings

### autoremove_old_entries (default: false)

When this setting is `true`, Colette will automatically remove completed fixed-deadline tasks or fixed-deadline tasks with passed due dates from the todo list on launch.

### debug_msg_color (default: CYAN)

Sets the display color(s) for debug messages. See [Color options](#color-options) for available values.

### enable_reminders (default: true)

By default, Colette prints due date reminders for tasks with due dates either today or tomorrow. Add this setting to your configuration file and set it to `false` to disable due date reminders.

### error_msg_color (default: RED)

Sets the display color(s) for error messages. See [Color options](#color-options) for available values.

### print_header_separator (default: true)

By default, Colette prints a separator line between the table header and the task list in the output of the **[list](./cmd/list.md)** command. Set this to `false` to disable printing the separator line.

### prompt_msg_color (default: GREEN)

Sets the display color(s) for the text in interactive prompts. See [Color options](#color-options) for available values.

### reminder_msg_color (default: YELLOW)

Sets the display color(s) for task reminder messages. See [Color options](#color-options) for available values.

### start_in_debug_mode (default: false)

When this setting is `true`, Colette will automatically start in debug mode. Colette's debug mode effectively acts like a verbose mode, printing additional messages in the terminal with extra information about what the program is doing internally.

### start_in_test_mode (default: false)

When this setting is `true`, Colette will automatically start in test mode. When test mode is on, any changes made to entries will remain strictly in memory and will not be written to the todo.clt file. Useful when you want to test Colette without messing up your todo.clt file.

### table_header_color (default: NULL)

Sets the display color(s) for the table header in the output of the **[list](./cmd/list.md)** command. See [Color options](#color-options) for available values.

### task_completed_color (default: GREEN)

Sets the display color(s) for completed tasks in the output of the **[list](./cmd/list.md)** command. See [Color options](#color-options) for available values.

### task_due_soon_color (default: BLACK + REDB)

Sets the display color(s) for tasks with due dates either today or tomorrow in the output of the **[list](./cmd/list.md)** command. See [Color options](#color-options) for available values.

### task_expired_color (default: BLACK + PURPLEB)

Sets the display color(s) for tasks with passed due dates in the output of the **[list](./cmd/list.md)** command. See [Color options](#color-options) for available values.

### warning_msg_color (default: YELLOW)

Sets the display color(s) for warning messages. See [Color options](#color-options) for available values.

## Color options

The following options are available for configuring the colors in Colette. Enclose them in either single quotes (') or double quotes (") when setting them in colette.toml. Options without B at the end set the color for the text itself, while options with B at the end set the background color. Text and background colors can be combined by concatenating them with a + symbol (**ex:** `"BLACK + GREENB"`).

Text colorization can also be disabled by passing `NULL` as a value for a color setting.

```text
BLACK
RED
GREEN
YELLOW
BLUE
PURPLE
CYAN
WHITE

BLACKB
REDB
GREENB
YELLOWB
BLUEB
PURPLEB
CYANB
WHITEB

NULL
```