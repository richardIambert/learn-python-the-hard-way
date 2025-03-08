# ex11.py - Asking Questions

# print("How old are you?", end=" ")
# age = input()

# print("How tall are you?", end=" ")
# height = input()

# print("How much do you weigh?", end=" ")
# weight = input()

# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Study Drills


def get_age():
    try:
        age = int(input("How old are you (years)? "))
        return age
    except ValueError:
        print("Please enter your age in years")
        return get_age()


def get_height():
    try:
        height = float(input("How tall are you (metres)? "))
        return height
    except ValueError:
        print("Please enter your height in metres")
        return get_height()


def get_weight():
    try:
        weight = float(input("How much do you weigh (kilograms)? "))
        return weight
    except ValueError:
        print("Please enter your weight in kilograms")
        return get_weight()


age_years = get_age()
height_metres = get_height()
weight_kilograms = get_weight()
print(
    f"So, you're {age_years} years old, {height_metres} metres tall, and weigh {weight_kilograms} kilograms."
)
