'''
    configHandler.py

    Handles reading information from a configuration file
    if one is found in the working directory or ~/.config/
    on launch.
'''

import tomllib
import os

conf_path = os.path.expanduser('~/.config/')
conf_name = 'colette.toml'

def get_config_file():
    return True if os.path.exists(conf_name) or os.path.exists(conf_path + conf_name) else False

def read_config_file():
    if get_config_file() == True:
        if os.path.exists(conf_path + conf_name):
            with open(conf_path + conf_name, 'rb') as conf:
                parsed_conf = tomllib.load(conf)
        elif os.path.exists(conf_name):
            with open(conf_name, 'rb') as conf:
                parsed_conf = tomllib.load(conf)

        return parsed_conf

def get_option(key: str):
    return read_config_file().get(key)

if __name__ == "__main__":
    print(get_config_file())
    print(read_config_file())

    if get_config_file():
        print(get_option('autoremove_old_entries'))
        print(get_option('enable_reminders'))
