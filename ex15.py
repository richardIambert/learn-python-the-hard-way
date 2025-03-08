# ex15.py - Reading Files

from sys import argv  # Import argv from sys module.

try:
    # Unpack elements of argv.
    script, filename = argv
    # Open a file, with a path value of that assigned to `filename`.
    # Assign the returned file object to a variable named `file`.
    # `open` will throw a `FileNotFoundError` if no file exists.
    file = open(filename)
    # Print the contents of the file by calling `file`'s `read` method.
    print(f"Here's your file {filename}:")
    # The `read` method also throws errors but we dont handle them here.
    print(file.read())
    # Ensure file is correctly closed by calling `file`'s `close` method.
    file.close()

    # Reprompt for another filename and repeat as above.
    new_filename = input("Type the filename again:\n> ")
    new_file = open(new_filename)
    print(f"Here's your file {new_filename}:")
    print(new_file.read())
    file.close()

# Catch and handle some errors that might thrown above.
except ValueError:
    # If script is called without a filename argument.
    # Attempting to unpack argv with more or less elements than expected.
    print("Filename argument is required")
except FileNotFoundError:
    # If a file with the passed filename argument isn't found.
    print("File not found")
