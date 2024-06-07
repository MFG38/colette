# Basic usage

---

## The prompt

As Colette is a terminal-based application, its main component is the command prompt. Colette is operated by typing commands into said prompt. You will find a list of supported commands below. Typing an unsupported command into the prompt will do nothing beside printing an error message.

## The todo file

Colette stores entries in the todo list into a special file named **todo.clt**. This file effectively stores the todo list, and Colette will load the entries from the file into memory if it finds one in the working directory. If Colette cannot find a todo file upon launching, it will generate an empty one in the working directory.

**NOTE:** The todo file is essentially a regular text file, storing the information that Colette needs to parse for each entry line by line. Colette does not encrypt this information in any manner, meaning that it is human-readable and rather easy to modify. That said, editing the todo file by hand is **NOT RECOMMENDED**, as doing so could lead to fatal errors. If you do wish to edit the todo file by hand, you will find a breakdown of its structure on the **[todo.clt breakdown](./technical/todo_clt.md)** page.

## Commands

Below is a list of the commands that Colette supports. See each command's dedicated documentation page for usage instructions. Parts of the commands enclosed in parentheses are optional.

- [add](./cmd/add.md)
- [a(uto)rem(ove)](./cmd/autoremove.md)
- [clear](./cmd/clear.md)
- [complete](./cmd/complete.md)
- [debug](./cmd/debug.md)
- [edit](./cmd/edit.md)
- [exit/quit](./cmd/exit_quit.md)
- [help](./cmd/help.md)
- [list](./cmd/list.md)
- [rem(ove)](./cmd/remove.md)
- [search](./cmd/search.md)
- [sort](./cmd/sort.md)
- [ver(sion)](./cmd/version.md)