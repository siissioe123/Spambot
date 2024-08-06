""" 
    This is a program to spam text
    Copyright (C) 2024  Siissioe123

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pyautogui
import threading
import time
import toml
import sys
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Configuration file name
config_file = 'config.toml'

# Load/initialize the config file
def load_config():
    try:
        with open(config_file, 'r') as file:
            config = toml.load(file)
    except FileNotFoundError:
        config = {'countdown': 5}
        save_config(config)
    return config

# Save config to the file
def save_config(config):
    with open(config_file, 'w') as file:
        toml.dump(config, file)

# Countdown 
def countdown_timer(seconds):
    while seconds:
        print(f'Countdown: {seconds}', end='\r')
        time.sleep(1)
        seconds -= 1

# Spamming the message
def spam_message(message, count):
    for _ in range(count):
        pyautogui.typewrite(message)
        pyautogui.press("enter")

# Display help message
def display_help():
    help_message = (
        "Usage: python main.py [options]\n\n"
        "Options:\n"
        "  -h, --help               Show this help message and exit\n"
        "  -c <seconds>             Set the countdown timer (default is 5 seconds)\n"
        "  -show w                  Show copyright information\n"
    )
    print(help_message)

# Copyright information
def show_copyright():
    print("""   This is a program to spam text
    Copyright (C) 2024  Siissioe123

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.""")

# Main 
def main():
    # Default confug
    config = load_config()

    # Parse command line arguments
    args = sys.argv[1:]
    if "-h" in args or "--help" in args:
        display_help()
        return
    if "-show" in args and "w" in args:
        show_copyright()
        return
    if "-c" in args:
        try:
            index = args.index("-c")
            countdown_value = int(args[index + 1])
            config['countdown'] = countdown_value
            save_config(config)
            print(f"Countdown set to {countdown_value} seconds")
        except (IndexError, ValueError):
            print(Fore.YELLOW + "Invalid countdown value. Using default value.")

    # Print header
    print("""    Spambot  Copyright (C) 2024  Siissioe123
    This program comes with ABSOLUTELY NO WARRANTY; for details use flag `-show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; use flag `-show w' for details.""")
    print('-' * 79)

    # Request message to spam
    message = input("\nEnter the message to spam (leave blank to quit, type 'show w' for info): ")
    if not message:
        print("No message entered. Exiting.")
        return
    if message == "show w":
        show_copyright()
        return

    # Request number of times to spam the message
    while True:
        try:
            count = int(input("Enter the number of times to spam the message: "))
            break
        except ValueError:
            print(Fore.YELLOW + "Please enter a valid number.")

    # Start countdown before spamming
    print(f"\nStarting in {config['countdown']} seconds...")
    countdown_thread = threading.Thread(target=countdown_timer, args=(config['countdown'],))
    countdown_thread.start()
    countdown_thread.join()

    # Warning message before the spam
    print(Fore.GREEN + Style.BRIGHT + "\nFire in the hole!")

    # Execute the spam
    spam_thread = threading.Thread(target=spam_message, args=(message, count))
    spam_thread.start()
    spam_thread.join()

if __name__ == "__main__":
    main()
