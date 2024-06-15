# Colette

**Colette** is a todo list manager that runs in the command line. It aims to be quick and simple to use while providing enough features to satisfy the needs of every command line lover.

Here's a list of Colette's main features:

- **Pure Python** - Colette is written in pure Python with no dependencies other than Python itself.
- **Simple but powerful list management** - Add, remove and edit entries, mark them as completed, sort your todo list etc.
- **Easy storage** - Colette stores the todo list into a human-readable file that can be modified with a text editor if desired.
- **Configurability** - Colette is configurable with a TOML file.

## Installation

### From the archive (Linux)

1. Download **colette-*.zip** from the Releases section of the GitHub repository.
2. Unzip the entire contents of colette-*.zip to a folder of your choice.
3. Add the following line to your shell configuration file:

    `PATH=$PATH:/path/to/extracted/binary`

Once you have performed the steps above, you can launch Colette by simply typing `colette` into the terminal.

### From source (Linux / macOS / Windows)

Refer to the instructions in the **[Building Colette](#building-colette)** section.

## Usage

Launch Colette and type `help` for a list of commands supported by Colette.

## Building Colette

### Dependencies

For building from source, Colette has the following dependencies:
* [Python](https://www.python.org/) 3.11 or newer version (3.11.2 is the lowest tested version. Latest version recommended.)
* [pip](https://pypi.org/project/pip/) or [pipx](https://github.com/pypa/pipx)
* [PyInstaller](https://pyinstaller.org/)
* [mkdocs](https://www.mkdocs.org/)

Install all of the dependencies as instructed for your operating system before building Colette. You can run the following command to install the dependencies:

    pip(x) install -r requirements.txt

### Running the build script

An automated build script named **build.sh** is supplied with Colette's source code. This is the recommended way to build Colette and its documentation from source.

You may need to make the build script executable before being able to run it. If the script fails to execute, it is likely that you do not have execution permissions for it yet. In that case, make it executable with the following command:

    chmod +x build.sh

After making the script executable, run it like so:

    ./build.sh

### Running Colette

After building Colette, you can run it by navigating into one of the directories generated by PyInstaller (either **build/colette/** or **dist/colette/**) and typing the following command:

    ./colette

You can also run Colette without building it by running the **main.py** file from the **src/** directory.

## Compatibility

### For building

|OS (Build system)      |Buildable?     |Supported? |Known issues           |
|-----------------------|---------------|-----------|-----------------------|
|**Linux**              |Yes            |Yes        |None                   |
|**macOS**              |Untested       |Partially  |None                   |
|**Windows**            |Yes            |No         |None                   |
|**Windows (Cygwin)**   |Untested       |No         |None                   |

### For running

**NOTE:** The table below contains only the terminals Colette has been tested in. If you don't see your terminal in the table, Colette has likely not been tested in it. Compatibility is not guaranteed in this case.

|Terminal                   |Runnable?      |Supported? |Known issues           |
|---------------------------|---------------|-----------|-----------------------|
|**PowerShell**             |Yes            |No         |Text color codes render as plain text on Windows. Setting text colors to NULL in colette.toml is a supported workaround.     |
|**Windows Command Prompt** |Yes            |No         |Text color codes render as plain text. Setting text colors to NULL in colette.toml is a supported workaround.     |
|**xterm**                  |Yes            |Yes        |None                   |

## License

Colette is licensed under MIT. See the [LICENSE](./LICENSE) file for details.

## Credits

This project uses code from the following resources:
* [console-color](https://gist.github.com/kamito/704813) Gist by kamito