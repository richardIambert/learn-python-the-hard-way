# ex30.py - Else and If

# We should take the cars.
# Maybe we could take the trucks.
# Alright, let's just take the trucks.

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")  # this will run
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")  # this will run
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")  # this will run
else:
    print("Fine, let's stay home then.")
