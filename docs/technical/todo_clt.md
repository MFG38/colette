# todo.clt breakdown

---

Colette stores the todo list in a special file named **todo.clt**. If Colette finds a todo file in the working directory on launch, it will read the file and load the entries from it into memory. The entries can then be modified from within the program, and any changes made to them will be written to the same file.

If a todo file is not found in the working directory on launch, Colette will generate an empty one.

## The structure of the file

todo.clt is essentially a regular text file but with a unique file extension. It stores the information for each entry line by line with no encryption or obfuscation, meaning that the information can be read by human beings as well as Colette itself.

Below is a sample of what the contents of todo.clt might look like:

```
pay rent,3,2024-06-15,0
send important email,0,2024-06-30,0
send monthly report,0,2024-05-31,1
brush teeth,1,2024-06-08,1
```

As you can see, each entry in the todo list is stored as plain text on its own line in the file. Each entry has four "columns" of information separated by commas; this information is what Colette parses and displays when the **[list](../cmd/list.md)** command is used. The four columns, in order from left to right, are the **description**, **type**, **due date** and **status** of each entry.

### Description

The first column of a line stores the description of an entry. This is stored as a plain-text string up to 60 characters long.

**NOTE:** Because the columns are separated by commas, a description cannot include a comma when entered from the interactive prompt of the **[add](../cmd/add.md)** command, as Colette will not parse the remaining information as intended and will likely crash. As of yet, there is no solution implemented to get around this limitation. If editing the todo file by hand, enclosing the description string in single quotes (') *might* work as a solution; however, this has been untested.

### Type

The second column of a line stores the type of an entry. This is stored as an integer value between 0 and 3, where the integers translate to the type strings shown in the output of the **[list](../cmd/list.md)** command as follows:

- 0 = fixed
- 1 = daily
- 2 = weekly
- 3 = monthly

Integer values beyond the listed ones will be parsed as unknown types but are not fatal.

### Due date

The third column of a line stores the due date of an entry. This is stored as a datetime value in ISO 8601 format (YYYY-MM-DD), parsed from the user's input when the **[add](../cmd/add.md)** command is run. See the documentation page of the **add** command for valid inputs.

If a task is of a non-fixed type and its due date has passed, Colette will update the due date based on its type on launch. The task will also be marked as incomplete if it was previously marked as completed.

### Status

The fourth and final column of a line stores the status of an entry. This is stored as an integer value of either 0 or 1, where 0 means "incomplete" and 1 means "completed". Values beyond 1 will be parsed as the task being completed and are not fatal.

The status is only used by Colette internally and never shown explicitly to the user. Tasks marked as completed, i.e. with a status value of 1 or more, will be printed in green in the output of the **[list](../cmd/list.md)** command.