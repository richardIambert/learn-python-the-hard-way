# ex31.py - Making Decisions

print("You enter a dark room with three doors.")
print("Do you go through door #1, door #2, or door #3?")
door = input("> ")

if door == "1":
    print("There's a giant bear in here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
elif door == "2":
    print("You stare into the endless abyss of Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of mush.")
        print("Good job!")
elif door == "3":
    print("You wake from your dream.")
    print("1. Get out of bed.")
    print("2. Stay in bed.")
    dream = input("> ")

    if dream == "1":
        print("You're bedroom is hell and the floor is lava. Well done!")
    elif dream == "2":
        print("You lay there for eternity. Well done!")
    else:
        print(f"Well, doing {dream} is probably better.")
else:
    print("You stumble around and fall on a knife and die. Good job!")
