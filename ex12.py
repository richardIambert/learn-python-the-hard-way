# ex12.py - Prompting People

# age = input("How old are you? ")
# height = input("How tall are you? ")
# weight = input("How much do you weigh? ")

# print(
#     f"So, you're {age} old, {height} tall and {weight} heavy."
# )  # A very American way of putting it...


def pounds_to_kilograms(pounds):
    return pounds / 2.20462262


def inches_to_centimetres(inches):
    return inches * 2.54


def inches_to_metres(inches):
    return inches * 0.0254


def prompt_age_years(
    prompt="How old are you?", reprompt="Please enter your age in years"
):
    try:
        age_years = int(input(f"{prompt} "))
        return age_years
    except ValueError:
        print(reprompt)
        return prompt_age_years(prompt, reprompt)


def prompt_height_inches(
    prompt="How tall are you (inches)? ", reprompt="Please enter your height in inches"
):
    try:
        height_inches = float(input(f"{prompt} "))
        return height_inches
    except ValueError:
        print(reprompt)
        return prompt_height_inches(prompt, reprompt)


def prompt_weight_pounds(
    prompt="How much do you weigh (pounds)?",
    reprompt="Please enter your weight in pounds",
):
    try:
        weight_pounds = float(input(f"{prompt} "))
        return weight_pounds
    except ValueError:
        print(reprompt)
        return prompt_weight_pounds(prompt, reprompt)


age_years = prompt_age_years()
height_inches = prompt_height_inches()
weight_pounds = prompt_weight_pounds()

height_metres = inches_to_metres(height_inches)
weight_kilograms = pounds_to_kilograms(weight_pounds)

print(
    f"So, you're {age_years} years old, {round(height_metres, 2)} metres tall, and weigh {round(weight_kilograms, 2)} kilograms."
)
