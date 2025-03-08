# ex6.py - Strings and Text

# Declare a variable named `types_of_people` and assign it the value 10
types_of_people = 10
# Declare a variable named `x` and assign it an f-string value
x = f"There are {types_of_people} types of people."

# Declare a variable named `binary` and assign it the string literal "binary"
binary = "binary"
# Declare a variable named `do_not` and assign it a the string literal "don't"
do_not = "don't"
# Declare a variable named `y` and a assign it an f-string value
y = f"Those who know {binary} and those who {do_not}."

# Print the value of `x`
print(x)
# Print the value of `y`
print(y)

# Print the value of an f-string
print(f"I said: {x}")
# Print the value of an f-string
print(f"I also said: '{y}'")

# Declare a variable named `hilarious` and assign it the value False
hilarious = False
# Delare a variable named `joke_evaluation` and assign it a string value with a format placeholder
joke_evaluation = "Isn't that joke so funny?! {}"
# Print the value of a formatted string
print(joke_evaluation.format(hilarious))

# Declare a variable `w` and assign it a string value
w = "This is the left side of..."
# Declare a variable `e` and assign it a string value
e = "a string with a right side."
# Print the values of `w` and `e`, concatenated
print(w + e)
