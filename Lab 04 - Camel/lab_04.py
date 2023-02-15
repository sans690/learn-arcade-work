import random


def main():
    MILES_TRAVELED = 0
    CAMEL_TIREDNESS = 0
    NATIVES_BEHIND_YOU = -20
    FULL_SPEED = random.randrange(10, 21)
    MODERATE_SPEED = random.randrange(5, 13)
    DRINKS_IN_CANTEEN = 3
    CAMEL_THIRST = 0
    USER_THIRST = 0

    # initial print statement to user
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives.\n")

    # game not done
    DONE = False
    while not DONE:

        # choices for user to pick from
        print("A. Drink from your canteen. ")
        print("B. Ahead moderate speed. ")
        print("C. Ahead full speed. ")
        print("D. Stop for the night. ")
        print("E. Status check. ")
        print("Q. Quit.")

        # user is asked question and gives a response
        USER_INPUT = input("What is your choice?")

        # user picks e = status
        # need moderate and full speed to be printed as miles when e is selected
        if USER_INPUT.upper() == "E":
            print("\nMiles traveled:", MILES_TRAVELED)
            print("Drinks in canteen:", DRINKS_IN_CANTEEN)
            # miles that natives are behind user
            print("The natives are", MILES_TRAVELED - NATIVES_BEHIND_YOU, "miles behind you.\n")

        # user picks q = quit
        elif USER_INPUT.upper() == "Q":
            print("\nGame will end now!")
            # End game
            DONE = True

        # user picks d = rest for night
        elif USER_INPUT.upper() == "D":
            CAMEL_TIREDNESS = 0
            print("\nCamel is happy.")
            NATIVES_BEHIND_YOU = NATIVES_BEHIND_YOU + random.randrange(7, 15)
            print("The native are now", MILES_TRAVELED - NATIVES_BEHIND_YOU, "miles behind you.\n")

        # user picks c = full speed
        elif USER_INPUT.upper() == "C":
            print("\nYou travel", MILES_TRAVELED + FULL_SPEED, "miles.")
            CAMEL_THIRST = CAMEL_THIRST + 1
            print("Camel's thirst is", CAMEL_THIRST)
            USER_THIRST = USER_THIRST + 1
            print("Your thirst is", USER_THIRST)
            CAMEL_TIREDNESS = CAMEL_TIREDNESS + 1
            print("Camel's tiredness is", CAMEL_TIREDNESS)
            NATIVES_BEHIND_YOU = NATIVES_BEHIND_YOU + random.randrange(7, 15)
            print("The native are now", MILES_TRAVELED - NATIVES_BEHIND_YOU, "miles behind you.\n")

        # user picks b = moderate speed
        elif USER_INPUT.upper() == "B":
            print("The native are now", MILES_TRAVELED + MODERATE_SPEED, "miles behind you.\n")
            print("\nYou travel", MODERATE_SPEED, "miles.")
            CAMEL_THIRST = CAMEL_THIRST + 1
            print("Camel's thirst is", CAMEL_THIRST)
            USER_THIRST = USER_THIRST + 1
            print("Your thirst is", USER_THIRST)

        # user picks a = drink from canteen
        elif USER_INPUT.upper() == "A":
            USER_INPUT_YORN = input("Do you take a drink?")
            if USER_INPUT_YORN.upper() == "YES" or USER_INPUT_YORN.upper() == "Y":
                DRINKS_IN_CANTEEN = DRINKS_IN_CANTEEN - 1
                print("\nYou have", DRINKS_IN_CANTEEN, "drinks left in canteen.")
                DRINKS_IN_CANTEEN - 1
                if USER_THIRST < 0:
                    print("You are not thirsty.")
                elif USER_THIRST > 0:
                    USER_THIRST = USER_THIRST - 1
                    print("Your thirst is", USER_THIRST, "\n")
            else:
                print("\nERROR.\n")

        # natives are close
        if NATIVES_BEHIND_YOU < 15 and not DONE:
            print("The natives are close!\n")
        # you are thirsty
        if USER_THIRST == 4 or USER_THIRST == 5 and not DONE and not USER_INPUT.upper() == "E":
            print("You are thirsty!")

        # you die of thirst
        if USER_THIRST > 6 and not DONE:
            print("You died of thirst!")
            exit()

        # camel is tired
        if CAMEL_TIREDNESS > 5 and not DONE and not USER_INPUT.upper() == "E":
            print("Your camel is getting tired.")

        # camel dies of exhaustion
        if CAMEL_TIREDNESS > 8 and not DONE:
            print("Your camel is died of exhaustion!")
            DONE = True

        # natives caught you
        if NATIVES_BEHIND_YOU == 0 and not DONE:
            print("The natives have caught up!")
            DONE = True

        # camel is thirsty
        if CAMEL_THIRST == 4 or CAMEL_THIRST == 5 and not DONE and not USER_INPUT.upper() == "E":
            print("Your camel is getting thirsty!")

        # camel dies of thirst
        elif CAMEL_THIRST > 8 and not DONE:
            print("Your camel died of thirst!")
            DONE = True

        # you beat the game
        if MILES_TRAVELED >= 200 and not DONE:
            print("\nYou win!\n")
            DONE = True

        # 1 / 20 of finding an oasis
        if not DONE and random.randrange(1, 21) == 1:
            if USER_INPUT.upper() == "E":
                continue
            else:
                print("\nYou found an oasis!")
            if CAMEL_TIREDNESS > 0:
                CAMEL_TIREDNESS = 0
                print("Your camel is no longer tired.")
            elif CAMEL_TIREDNESS == 0:
                print("Your camel's tiredness is already at zero.")
            if USER_THIRST > 0:
                USER_THIRST = 0
                print("You are no longer thirsty.")
            elif USER_THIRST == 0:
                print("You drank water, and it did nothing.")
            if DRINKS_IN_CANTEEN == 3:
                print("Your canteen is already at max.\n")
            elif DRINKS_IN_CANTEEN == 0 or DRINKS_IN_CANTEEN == 1 or DRINKS_IN_CANTEEN == 2:
                print("You refill your canteen.\n")
                DRINKS_IN_CANTEEN = 3
            else:
                print("You found nothing.\n")


main()
