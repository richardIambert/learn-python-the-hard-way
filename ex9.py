# ex9.py - Printing, Printing, Printing

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"  # \n escape character represents a newline in a string

print("Here are the days: ", days)
print("Here are the months: ", months)

# Triple quotes (double or single) create a multi-line string.
# Whitespace is maintained within a multi-line string.
# Prepend multi-line strings with an `f` to create a multi-line f-string.
print(
    """
There's something going on here.
With the three double-quotes.
We'll be able to type as mucn as we like.
Even 4 lines if we want, or 5, or 6.
"""
)
