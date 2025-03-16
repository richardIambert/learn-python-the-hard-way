# ex36.py - Designing and Debugging

from sys import exit

start_items = ["torch", "hairspray", "tasty snack", "sword", "rope"]
player_inventory = []
merchant_inventory = [
    "golden dagger",
    "night-vision goggles",
    "rusty key",
    "worn rope",
    "bacon",
    "map",
]


def two_paths():
    print("Wandering deeper into the cave, you see it separates into two paths.")
    print("Take the left path or the right?")
    choice = input("> ")

    if choice == "left":
        if "torch" in player_inventory:
            print("You shine your torch and avoid the spike pit.")
            pooch_encounter()
        else:
            die("It's too dark! You fall into a spike pit and die.")
    elif choice == "right":
        pooch_encounter()
    elif choice == "go back":
        print("There is no going back you whammer!")
        two_paths()
    else:
        print("I've no idea what that means.")
        die("You try to venture off script and die.")


def pooch_encounter():
    print("You happen upon a scruffy looking pooch that needs your help.")

    if "tasty snack" in player_inventory:
        print("He seems very hungry...")
        print("Feed the pooch or leave the pooch?")
        choice = input("> ")
        if "feed" in choice:
            print("The pooch becomes your trusty companion!")
            print("Off you wander hand in paw!")
            player_inventory.append("trusty pooch")
            player_inventory.pop(player_inventory.index("tasty snack"))
            snake_encounter()
        elif "leave" in choice:
            print("Yikes! He's actually a ware-bear in bad light!")
            die("He bites your head clean off and you die.")
        else:
            print("I've no idea what that means.")
            die("You try to venture off script and die.")
    elif "rusty sword" in player_inventory:
        print("Hell's Bells! The pooch is actually a ware-bear!")
        print("Fight or flight?")
        choice = input("> ")

        if "fight" in choice:
            print("You slay the ware-pooch but your sword is damaged in the fight.")
            print("Sword removed from inventory.")
            have_sword = False
            merchant_encounter()
        elif "flight" in choice or "run" in choice or "flee" in choice:
            print("You are the lamest adventurer ever...")
            print("You slip into a side cave and all is well.")
            merchant_encounter()
        else:
            print("I've no idea what that means.")
            die("You try to venture off script and die.")


def snake_encounter():
    print("BJeezus! A snake!")
    if "pooch" in player_inventory:
        print("Your trusty pooch leaps into action!")
        print("Left paw!")
        print("Right paw!")
        print("South paw!")
        print("The snake is no more... Moving on!")
        merchant_encounter()


def merchant_encounter():
    print("You come across a merchant selling all manner of wares...")
    print("but not ware-pooches, thankfully!")
    trade_items()


def monster_encounter():
    pass


def list_start_items():
    print("Start items:")
    for item, index in start_items:
        print(f"{index + 1}. {item}")


def list_player_inventory():
    print("Player inventory:")
    for item, index in player_inventory:
        print(f"{index + 1}. {item}")


def list_merchant_inventory():
    print("Merchant inventory:")
    for item, index in merchant_inventory:
        print(f"{index + 1}. {item}")


def choose_start_items():
    try:
        list_start_items()
        index_strings = input(
            "Choose three items to start your (not)adventure (e.g, 1,2,3): "
        )
        index_numbers = index_strings.split(",")
        if len(index_numbers) != 3:
            raise ValueError
        for index_number in index_numbers:
            player_inventory.append(start_items[int(index_number)])
        list_player_inventory()
    except ValueError:
        print("Nope...")
        return choose_start_items()


def trade_items():
    list_player_inventory()
    list_merchant_inventory()
    trade = input("Trade items (y/n)? ")

    if trade == "y":
        try:
            give_item = player_inventory.pop(
                int(input(f"Item to give (1 - {len(player_inventory)})> ")) - 1
            )
            take_item = merchant_inventory.pop(
                int(input(f"Item to take (1 - {len(merchant_inventory)})> ")) - 1
            )
            merchant_inventory.append(give_item)
            player_inventory.append(take_item)
            monster_encounter()
        except ValueError:
            die("You try to break my poorly tested game and die.")
    elif trade == "n":
        print("Suit yourself. Onwards!")
        monster_encounter()
    else:
        print("I've no idea what that means.")
        die("You try to venture off script and die.")


def die(reason):
    print(f"{reason} Well done!")
    exit(0)


def start():
    print("It's Wednesday evening...")
    print("You're taking the wheelie bins out...")
    print(
        "You hear a bang and notice a light shining from the the green bin of horror..."
    )
    print("You go to investigate...")
    choose_start_items()
