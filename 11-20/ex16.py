# ex16.py - Reading and Writing Files

# Common file methods:
#
#    file.close() - Closes `file`.
#     file.read() - Reads and returns the contents of `file`.
# file.readline() - Reads a single line of a file.
# file.truncate() - Empties the contents of `file`.
# file.write(arg) - Writes arg to `file`.
#  file.seek(arg) - Moves to position arg in `file`.

# |H|e|l|l|o|,| |W|o|r|l|d|!|
#          ^
#          |
#     seek(4)

from sys import argv, exit
import os


def handle_keyboard_interrupt():
    print("Exiting...")
    exit(0)


def handle_existing_file(filename):
    print(f"{filename} already exists.")
    try:
        action = input("Append(a), Overwrite(o), Cancel(CTRL-C)? ")
        if action == "a":
            print(f"Appending to {filename}.")
            return open(filename, "a")
        elif action == "o":
            print(f"Overwriting {filename}.")
            return open(filename, "w")
        else:
            return handle_existing_file(filename)
    except KeyboardInterrupt:
        handle_keyboard_interrupt()


def handle_new_file(filename):
    print(f"Creating {filename}.")
    return open(filename, "w")


def write_lines(file):
    try:
        line1 = input("Line 1: ")
        line2 = input("Line 2: ")
        line3 = input("Line 3: ")
        lines = f"{line1}\n{line2}\n{line3}"
        print("Writing new lines to file.")
        file.write(lines)
        file.close()
        print("Write successful.")
    except KeyboardInterrupt:
        handle_keyboard_interrupt()


try:
    _, filename = argv
    if os.path.exists(filename):
        file = handle_existing_file(filename)
        write_lines(file)
    else:
        file = handle_new_file(filename)
        write_lines(file)
except ValueError:
    print("Argument filename is required.")
    exit(1)
