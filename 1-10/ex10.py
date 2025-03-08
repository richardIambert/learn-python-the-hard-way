# ex10.py - What Was That?

# Escape sequences are used to encode characters into a string that are difficult to type.

# Some common escape sequences include:
# \\ - Backslash \
# \' - Single-quote '
# \" - Double-quote "
# \n - Newline
# \t - Horizontal tab
# \uxxxx - 16-bit unicode
# \Uxxxxxxxx - 32-bit unicode

tabby_cat = "\tI'm tabbed in."  # \t escape sequence encodes a tab
persian_cat = "I'm split\non a line."  # \n escape sequence encodes a new line
backslash_cat = "I'm \\ a \\ cat."  # To encode a \ we need to escape the escape sequence prefix (\) with the escape sequence prefix...👀

# Escape sequences can be used in multi-line strings
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
