# ex33.py - While Loops

# # Setup a variable to use in our while loop conditional expression
# i = 0
# numbers = []

# # Conditional expression determines whether while loop code block runs
# # While i is less than 6...
# while i < 6:
#     # Do the thing...
#     # Show what i is at the start of the loop
#     print(f"At the top i is {i}")

#     # Adding the value of i to our numbers list in each iteration
#     numbers.append(i)
#     print(f"Numbers is now: {numbers}")

#     # Incrementing i ensures the loop eventually ends
#     i += 1
#     # Show what i is at the end of the loop
#     print(f"At the bottom i is {i}")


# print("The numbers:")
# for number in numbers:
#     print(number)


# Study Drills


def create_number_list(start, stop, step=1):
    """Creates a list of numbers from [start, stop), incrementing by step"""
    count = start
    numbers = []
    while count < stop:
        numbers.append(count)
        count += step
    return numbers


print(create_number_list(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(create_number_list(0, 11, 2))  # [0, 2, 4, 6, 8, 10]
print(create_number_list(1, 10, 3))  # [1, 4, 7]


def create_number_list_alt(start, stop, step=1):
    return [n for n in range(start, stop, step)]


print(create_number_list_alt(10, 0, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(create_number_list_alt(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(create_number_list_alt(0, 11, 2))  # [0, 2, 4, 6, 8, 10]
print(create_number_list_alt(1, 10, 3))  # [1, 4, 7]
