# Configuration

---

Colette is configurable through a TOML file. See the [TOML website](https://toml.io/en/) for more information and a syntax reference.

If you wish to configure Colette, create a file named **colette.toml** in the working directory and add any settings you wish to modify into that file. See **[Available settings](#available-settings)** for a list of configuration options.

## Available settings

### autoremove_old_entries (default: false)

When this setting is set to `true`, Colette will automatically remove completed fixed-deadline tasks or fixed-deadline tasks with passed due dates from the todo list on launch.

### enable_reminders (default: true)

By default, Colette prints due date reminders for tasks with due dates either today or tomorrow. Add this setting to your configuration file and set it to `false` to disable due date reminders.

### start_in_debug_mode (default: false)

When this setting is `true`, Colette will automatically start in debug mode. Colette's debug mode effectively acts like a verbose mode, printing additional messages in the terminal with extra information about what the program is doing internally.

### start_in_test_mode (default: false)

When this setting is `true`, Colette will automatically start in test mode. When test mode is on, any changes made to entries will remain strictly in memory and will not be written to the todo.clt file. Useful when you want to test Colette without messing up your todo.clt file.

## Color options

The following options are available for configuring the colors in Colette. Options without B at the end set the color for the text itself, while options with B at the end set the background color. Text and background colors can be combined by concatenating them with a + symbol (**ex:** `BLACK + GREENB`).

The `RESET` color code resets all colors to the default.

**NOTE:** This feature is non-functional and fatal for the time being.

```
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

RESET
```