import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def get_random_villain():
    villain_list = ["Gorgon", "Troll", "Pirate", "Witch", "Dragon"]
    enemy = random.choice(villain_list)
    return enemy

# def creature():
#     villain = get_random_villain()
# villain = get_random_villain()

def intro():
    global villain
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {villain} is somewhere around here, "
                f"and has been "
                "terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")


def game_restart():
    response = input("Would you like to play again? (y/n)\n").lower()
    if response == "y":
        play_game()
    if response == "n":
        print_pause("Have a great day :)")
        exit()
    else:
        print_pause("Invalid input, please try again. ")
        game_restart()


def field(items):
    response = input(
        "Enter 1 to knock on the door of the house.\n"
        "Press 2 to peer into the cave.\n")
    if response == "1":
        enter_house(items)
    elif response == "2":
        enter_cave(items)
    else:
        print_pause("Please try again.")
        field(items)


def enter_cave(items):
    if "Sword" in items:
        print_pause("You look into the familiar cave.")
        print_pause("Nothing has changed in the cave since you've been here "
                    "last.")
        print_pause("You walk back into the field.")
        field(items)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be a very small cave.")
        print_pause("Your eye catches a small glint of metal behind a rock.")
        print_pause("You investigate and find a dirty sword.")
        print_pause("You clean it off and realise that it is the magical "
                    "Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        items.append("sword")
        print_pause("You walk back into the field")
        field(items)


def enter_house(items):
    global villain
    print_pause("You approach the house")
    print_pause(f"You are about to knock when the door opens and out steps "
                f"a {villain}!")
    print_pause(f"EEP! This is the {villain}'s house!")
    print_pause(f"The {villain} lunges towards you!")
    fight(items)


def fight(items):
    if "sword" not in items:
        print_pause("You only have your old dagger with you, you feel vastly "
                    "unprepared.")
        print_pause("What would you like to do?")
    else:
        print_pause("What would you like to do?")
    response = input("Press 1 to run away.\nPress 2 to fight\n ")
    if response == "1":
        print_pause("You run away, fortunately you don't seem to have been "
                    "followed.")
        field(items)
    elif response == "2":
        if "sword" in items:
            global villain
            print_pause(f"As the {villain} moves to attack, you unsheathe "
                        f"your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand "
                        "as you brace yourself for the attack.")
            print_pause(f"But the {villain} takes one look at your shiny new "
                        f"sword and runs away!")
            print_pause(f"You have rid the town of the {villain}, you are "
                        f"victorious!")
            game_restart()
        else:
            print_pause("You do your best.")
            print_pause("You are defeated.")
            game_restart()
    else:
        print_pause("Please try again.")
        fight(items)


def play_game():
    global villain
    villain = get_random_villain()
    items = []
    intro()
    field(items)


play_game()
