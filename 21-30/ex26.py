from sys import argv, exit


def handle_clean_exit():
    print("Exiting")
    exit(0)


def get_age():
    try:
        age = int(input("How old are you (years)? "))
        return age
    except ValueError:
        print("Please enter your age in years")
        return get_age()
    except KeyboardInterrupt:
        handle_clean_exit()


def get_height():
    try:
        height = float(input("How tall are you (metres)? "))
        return height
    except ValueError:
        print("Please enter your height in metres")
        return get_height()
    except KeyboardInterrupt:
        handle_clean_exit()


def get_weight():
    try:
        weight = float(input("How much do you weigh (kilograms)?"))
        return weight
    except ValueError:
        print("Please enter your weight in kilograms")
        return get_weight()
    except KeyboardInterrupt:
        handle_clean_exit()


def print_bio(age, height, weight):
    print(
        f"So, you're {age} years old, {height} metres tall and weight {weight} kilograms."
    )


def get_script_arguments():
    try:
        _, filepath = argv
        return filepath
    except ValueError:
        print("Usage: python ex26.py <filepath>")


def prompt_for_filepath():
    try:
        filepath = input("Enter the filename you want to open: ")
        return filepath
    except KeyboardInterrupt:
        handle_clean_exit()


def open_and_print_file(filepath):
    try:
        with open(filepath) as file:
            print(f"Here's your file {filepath}:")
            print(file.read())
    except FileNotFoundError:
        print(f"{filepath} not found.")


age_years = get_age()
height_metres = get_height()
weight_kilograms = get_weight()
print_bio(age_years, height_metres, weight_kilograms)

filepath = get_script_arguments()
open_and_print_file(filepath)

filepath = prompt_for_filepath()
open_and_print_file(filepath)

print("Let's practice everything.")
print("You'd need to know 'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")
if people > cats:
    print("Not many cats! The world is saved!")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")
