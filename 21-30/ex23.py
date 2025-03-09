# ex23.py - Strings, Bytes, and Character Encodings

from sys import argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(f"{raw_bytes} <===> {cooked_string}")


try:
    script, filename, input_encoding, error = argv

    with open(filename, encoding="utf-8") as file:
        main(file, input_encoding, error)

except ValueError:
    print("Usage: python ex23.py <file_path> <input_encoding> <errors>")
except FileNotFoundError:
    print("Error: file not found")
