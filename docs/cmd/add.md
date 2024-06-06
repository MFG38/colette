# Commands: add

---

## Description

Launches an interactive prompt to add an entry to the todo list. The prompt will first ask for a description of the task, then a type, and finally its due date.

The description can be anything as long as it fits within 60 characters and does not contain a comma anywhere within it.

The type can be one of the following: **fixed**, **daily**, **weekly**, **monthly**. You can also enter only the initial of each type. Internally, the type string will be parsed into an integer as described:

- 0 = fixed
- 1 = daily
- 2 = weekly
- 3 = monthly

The due date can be provided as one of the following:

- A full date in YYYY-MM-DD format (**ex:** 2024-12-31)
- A month and day in MM-DD format (**ex:** 12-31)
- A weekday either typed in full or abbreviated to its first 3 letters, optionally preceded by "next" (**ex:** Tuesday, Sat, next Friday)
- "today" or "tomorrow"

The due date will be parsed based on its format and converted into a usable date internally. For tasks with non-fixed due dates, their due dates will get automatically updated upon launching Colette if the previous due date has passed.