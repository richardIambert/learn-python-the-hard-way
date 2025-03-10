# ex32.py - Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

# Different ways to create a list
# 1. Use a list literal
numbers = [1, 2, 3, 4, 5]
print("List literal")
for number in numbers:
    print(f"Number is: {number}")
# 2. Combine list constructor with range function
numbers = list(range(1, 6))
print("List constructor and range function")
for number in numbers:
    print(f"Number is: {number}")
# 3. Use a list comprehension
numbers = [x for x in range(1, 6)]
print("List comprehension")
for number in numbers:
    print(f"Number is: {number}")

# Some other list comprehension examples
doubles = [x * 2 for x in range(1, 6)]
print("1 - 5 doubled:")
for double in doubles:
    print(double)

squares = [x**2 for x in range(1, 6)]
print("1 - 5 squared")
for square in squares:
    print(square)
