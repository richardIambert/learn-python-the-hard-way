# ex7.py - More Printing

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format("snow"))
print("And everywhere that Mary went.")
print("." * 10)  # Create a string with the `.` character repeated 10 times.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch `end = ' '` at the end. Try removing it to see what happens.
# By default, `print` ends with a newline character and the values of subsequent `print` statements appear on a new line.
# Setting the `end` named argument to ' ' results in the printed values being output to the same line, separated by a space.
print(end1 + end2 + end3 + end4 + end5 + end6, end=" ")
print(end7 + end8 + end9 + end10 + end11 + end12)
