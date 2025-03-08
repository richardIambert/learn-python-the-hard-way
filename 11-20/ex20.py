# ex20.py - Functions and Files

from sys import argv


def print_all(file):
    print(file.read())


def rewind(file):
    file.seek(0)


def print_a_line(line_count, file):
    print(line_count, file.readline(), end="")


try:
    _, filename = argv

    file = open(filename)

    print("First let's print the whole file:\n")
    print_all(file)

    print("\nNow let's rewind, kind of like a tape.\n")
    rewind(file)

    print("Now let's print three lines:\n")
    for num in range(1, 4):
        print_a_line(num, file)

except ValueError:
    print("Usage: python ex20.py <filename>")
except FileNotFoundError:
    print("Error: File not found")
