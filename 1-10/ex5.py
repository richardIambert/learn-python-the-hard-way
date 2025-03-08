# ex5.py - More Variables and Printing

name = "Richard Lambert"
age = 37
height_inches = 70
weight_pounds = 180
eyes = "Hazel"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height_inches} inches tall.")
print(f"He weighs {weight_pounds} pounds.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height_inches + weight_pounds
print(f"If I add {age}, {height_inches}, and {weight_pounds} I get {total}")

# Study Drills
height_metres = height_inches * 0.0254
weight_kilograms = weight_pounds / 2.20462262
print(f"He's {round(height_metres, 2)} metres tall.")
print(f"He weighs {round(weight_kilograms, 2)} kilograms.")
