print("Welcome to Camel! You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! ")
print("Survive your desert trek and out run the natives.")

miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_behind = -20
drinks_in_canteen = 3
done = False


def program():
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        userInput = input("What is your choice? ")
        if userInput.upper() == "Q":
            exit()

        elif userInput.upper() == "E":
            print("Miles traveled: ", miles_traveled)
            print("Drinks in canteen: ", drinks_in_canteen)
            print("Your camel has ", camel_tiredness, "amount of fatigue.")
            print("The natives are ", natives_behind, "miles behind you.")
            print()


program()
