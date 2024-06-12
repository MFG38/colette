# Configuration

---

Colette is configurable through a TOML file placed in the working directory.

## Options

### autoremove_old_entries (default: false)

When this setting is set to `true`, Colette will (allegedly) automatically remove completed fixed-deadline tasks or fixed-deadline tasks with passed due dates from the todo list on launch. **NOTE:** This setting is non-functional at the moment.

### enable_reminders (default: true)

By default, Colette prints due date reminders for tasks with due dates either today or tomorrow. Add this setting to your configuration file and set it to `false` to disable due date reminders.

## Color options

The following options are available for configuring the colors in Colette. Options without B at the end set the color for the text itself, while options with B at the end set the background color. Text and background colors can be combined by concatenating them with a + between them (**ex:** `BLACK + GREENB`).

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
```