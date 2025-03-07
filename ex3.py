# ex3.py - Numbers and Math

# a + b, addition, the sum of a + b
# a - b, subtraction, the difference of a - b
# a / b, division, the quotient of a / b
# a * b, multiplication, the product of a * b
# a % b, modulo, the remainder of a / b
# a < b, comparison, is a less than b
# a > b, comparison, is a greater than b
# a <= b, comparison, is a less than or equal to b
# a >= b, comparison, is a greater than or equal to b

# Arithmetic order of operations - PEDMAS, BIDMAS, BODMAS
# Parentheses, Exponents, Division, Multiplication, Addition, Subtraction

print("I will now ocunt my chickens:")

print("Hens", 25 + 30 / 6)  # 30
print("Roosters", 100 - 25 * 3 % 4)  # 97

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)  # 6.75

print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)  # False

print("What is 3 + 2?", 3 + 2)  # 5
print("What is 5 - 7?", 5 - 7)  # -2

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)  # True
print("Is it greater or equal?", 5 >= -2)  # True
print("Is it less or equal?", 5 <= -2)  # False

# Study Drills

degreesCelsius = 100
degreesFahrenheit = (degreesCelsius * 9 / 5) + 32
print(f"{degreesCelsius}°C equals {degreesFahrenheit}°F")
