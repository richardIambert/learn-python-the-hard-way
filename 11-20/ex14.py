# ex14.py - Prompting and Passing

from sys import argv

if len(argv) != 2:
    print(f"{argv[0]} requires a single name argument")
else:
    script, name = argv
    prompt = "> "

    print(f"Hi {name}, I'm the {script} script.")
    print("I'd like to ask you a few questions.")
    print(f"Do you like me {name}?")
    likes = input(prompt)

    print(f"Where do you live {name}?")
    lives = input(prompt)

    print("What kind of computer do you have?")
    computer = input(prompt)

    print(
        f"""
  Alright, so you said "{likes}" about liking me.
  You live in "{lives}". Not sure where that is.
  And you have a "{computer}" computer. Nice.
  """
    )
