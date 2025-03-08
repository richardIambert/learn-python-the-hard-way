# ex17.py - More Files

from sys import argv
from os.path import exists

script, from_filename, to_filename = argv

print(f"Copying from {from_filename} to {to_filename}.")

# We could do these two on one line, how?
# from_file_content = open(from_filename).read()
from_file = open(from_filename)
from_file_content = from_file.read()

print(f"{from_filename} is {len(from_file_content)} bytes long.")

print(f"Does the output file exist? {exists(to_filename)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()

to_file = open(to_filename, "w")
to_file.write(from_file_content)

print("Alright, all done.")
from_file.close()
to_file.close()
