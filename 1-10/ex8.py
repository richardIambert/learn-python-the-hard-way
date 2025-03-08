# ex8.py - Printing, Printing

# Declare a variable named `formatter` and assign it a string with 4 format placeholders
formatter = "{} {} {} {}"

# Call the `formatter` string's `format` function, passing in 4 arguments to match its placeholders
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(
    formatter.format(
        "Try your", "Own text here", "Maybe a poem", "Or a song about fear"
    )
)
