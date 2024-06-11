# Colette

**Colette** is a todo list manager that runs in the command line. It aims to be quick and simple to use while providing enough features to satisfy the needs of every command line lover.

Here's a list of Colette's main features:

- **Pure Python** - Colette is written in pure Python with no dependencies other than Python itself.
- **Simple but powerful list management** - Add, remove and edit entries, mark them as completed, sort your todo list etc.
- **Easy storage** - Colette stores the todo list into a human-readable file that can be modified with a text editor if desired.

## Installation

### From the archive

1. Download **colette-*.zip** from the Releases section of the GitHub repository.
2. Unzip the entire contents of colette-*.zip to a folder of your choice.
3. **(OPTIONAL)** Add the following line to your shell configuration file:

    `alias colette='cd /path/to/extracted/binary && ./colette'`

### From source

Refer to the instructions in the **[Building Colette](#building-colette)** section.

## Usage

Launch Colette with either `./colette` (requires building first) or `python src/main.py` and type `help` for a list of commands supported by Colette.

## Building Colette

### Dependencies

For building from source, Colette has the following dependencies:
* [Python](https://www.python.org/) 3.12.3 (Some older versions may be able to run Colette but have been untested. 3.10 is the bare minimum version.)
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

## License

Colette is licensed under MIT. See the [LICENSE](./LICENSE) file for details.

## Credits

This project uses code from the following resources:
* [console-color](https://gist.github.com/kamito/704813) Gist by kamito