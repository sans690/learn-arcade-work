import random

print("Welcome to Camel! You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! ")
print("Survive your desert trek and out run the natives.")

DONE = False


def main():
    MILES_TRAVELED = 0
    CAMEL_TIREDNESS = 0
    NATIVES_BEHIND_YOU = -20
    DRINKS_IN_CANTEEN = 0
    NATIVES_UP = random.randrange(7, 15)
    FULL_SPEED = random.randrange(10, 21)
    CAMEL_USES_ENERGY = + random.randrange(1, 4)
    MODERATE_SPEED = random.randrange(5, 13)
    DRINKS_IN_CANTEEN = 3
    YES_DRINK = DRINKS_IN_CANTEEN - 1
    CAMEL_THIRST = 0
    USER_THIRST = 0

    # choices for user to pick from
    print("A. Drink from your canteen. ")
    print("B. Ahead moderate speed. ")
    print("C. Ahead full speed. ")
    print("D. Stop for the night. ")
    print("E. Status check. ")
    print("Q. Quit. ")
    # user is asked question and gives a response
    USER_INPUT = input("What is your choice? ")
    # user picks e = status
    if USER_INPUT.upper() == "E":
        print("Miles traveled:", MILES_TRAVELED)
        print("Drinks in canteen:", DRINKS_IN_CANTEEN)
        # miles that natives are behind user
        NATIVES_BEHIND_YOU_NOW = MILES_TRAVELED - NATIVES_BEHIND_YOU
        print("The natives are", NATIVES_BEHIND_YOU_NOW, "miles behind you.")
    # user picks q = quit
    elif USER_INPUT.upper() == "Q":
        # End game
        DONE = True
    # user picks d = rest for night
    elif USER_INPUT.upper() == "D":
        CAMEL_TIREDNESS = 0
        print("Camel is happy!")
        NATIVES_UP = random.randrange(7, 15)
        print("The native are now", NATIVES_UP, "miles behind you.")
    # user picks c = full speed
    elif USER_INPUT.upper() == "C":
        print("You travel", FULL_SPEED, "miles")
        print("Camel's thirst is", CAMEL_THIRST + 1)
        print("Your thirst is", USER_THIRST + 1)
        print("Camel's tiredness is", CAMEL_TIREDNESS + 1)
        NATIVES_UP = random.randrange(7, 15)
        print("Natives move up", NATIVES_UP, "miles")
    # user picks b = moderate speed
    elif USER_INPUT.upper() == "B":
        print("You travel", MODERATE_SPEED, "miles.")
        print("Camel's thirst is", CAMEL_THIRST + 1)
        print("Your thirst is", USER_THIRST + 1)
        print("Natives move up", NATIVES_UP, "miles")
    # user picks a = drink from canteen
    elif USER_INPUT.upper() == "A":
        USER_INPUT_YORN = input("Do you take a drink? ")
        if USER_INPUT_YORN.upper() == "YES":
            print("You have", YES_DRINK, "drinks left in canteen. ")
            print("Your thirst is", USER_THIRST)
        else:
            print("ERROR. ")

    # you are thirsty
    if USER_THIRST > 4:
        print("You are thirsty! ")
    # you die of thirst
    if USER_THIRST > 6:
        print("You died of thirst! ")
        exit()
    # camel is tired
    if CAMEL_TIREDNESS > 5:
        print("Your camel is getting tired. ")
    # camel dies of exhaustion
    if CAMEL_TIREDNESS > 8:
        print("Your camel is dead of exhaustion!")
    # natives caught you
    if NATIVES_BEHIND_YOU == 0:
        print("The natives have caught up! ")
        exit()
    # camel is thirsty
    if CAMEL_THIRST > 5:
        print("Camel getting thirsty! ")
    # camel dies of thirst
    if CAMEL_THIRST > 8:
        print("Camel died of thirst! ")
    # you beat the game
    if MILES_TRAVELED == 200:
        print("You win!")
        DONE = True

    # 1 / 20 of finding an oasis
    for i in range(1):
        if random.randrange(2) == 1:
            print("You found an oasis! ")
            if CAMEL_TIREDNESS > 0:
                CAMEL_TIREDNESS = 0
                print("Your camel is no longer tired. ")
            elif CAMEL_TIREDNESS == 0:
                print("Your camel's tiredness is already at zero. ")
            if USER_THIRST > 0:
                USER_THIRST = 0
                print("You are no longer thirsty. ")
            elif USER_THIRST == 0:
                print("You drank water, and it did nothing. ")
            if DRINKS_IN_CANTEEN == 3:
                print("Your canteen is already at max. ")
            elif DRINKS_IN_CANTEEN == 0 or DRINKS_IN_CANTEEN == 1 or DRINKS_IN_CANTEEN == 2:
                print("You refill your canteen. ")
                DRINKS_IN_CANTEEN = 0
        else:
            print("Found nothing. ")


main()
