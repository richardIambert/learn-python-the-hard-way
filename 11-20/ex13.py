# ex13.py - Parameters, Unpacking, Variables

from sys import argv  # import argv from sys module

# # unpacking argv - similar to array destructuring in JavaScript
# script, first, second, third = argv

# print(f"The script is called: {script}")
# print(f"Your first variable is: {first}")
# print(f"Your second variable is: {second}")
# print(f"Your third variable is: {third}")

script, bottle_count = argv


def bottle_or_bottles(count):
    return "bottle" if count == 1 else "bottles"


def lets_go_green_bottles(number):
    if number > 0:
        print(
            f"""
{number} green {bottle_or_bottles(number)}, sitting on the waaalll...
And if 1 green botttllleee should yada yada yada...
There'd be {number - 1} green {bottle_or_bottles(number - 1)} sitting on the waaalll...
"""
        )
        lets_go_green_bottles(number - 1)


try:
    lets_go_green_bottles(int(bottle_count))
except ValueError:
    print("First argument must be a number")
