# ex29.py - What If

# Too many cats! The world is doomed!
# The world is dry!
# People are greater than or equal to dogs.
# People are less than or equal to dogs.
# People are dogs.

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")  # this will run

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")  # this will run


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")  # this will run

if people <= dogs:
    print("People are less than or equal to dogs.")  # this will run

if people == dogs:
    print("People are dogs.")  # this will run
