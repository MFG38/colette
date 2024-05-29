# Colette documentation

---

## Introduction

**Colette** is a WIP todo list manager that runs in the command line.

## Building Colette

As of yet, there is no readily provided building solution for Colette. That said, if you want to build Colette as a stand-alone application, you can probably do so using **PyInstaller** or something similar. A build script for Colette will be provided when the first stable version of the application is ready to be shipped.

## Using Colette

### Dependencies

Colette has the following dependencies:

- Python 3.12.3 (Some older versions may be able to run Colette but have been untested. 3.10 is the bare minimum version.)

### Running Colette

Running Colette is as simple as running `main.py` from the **src/** directory.

### Commands

Below is a list of the commands that Colette supports. See each command's dedicated documentation page for usage instructions.

- [add](./cmd/add.md)
- [clear](./cmd/clear.md)
- [edit](./cmd/edit.md)
- [exit](./cmd/exit.md)
- [help](./cmd/help.md)
- [list](./cmd/list.md)
- [rem(ove)](./cmd/remove.md)
- [search](./cmd/search.md)
- [ver(sion)](./cmd/version.md)

## License

Colette is licensed under the MIT license.