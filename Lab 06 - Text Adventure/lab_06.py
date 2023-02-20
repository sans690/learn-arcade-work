class Room:

    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


# creating instances of rooms in the class
def main():
    # the current room is bedroom 1, which is 0
    current_room = 0
    # defining what rooms there are and adding them to the list
    room_list = []
    room_0 = Room("You are in the second bedroom.\nThere is a door to the east.", None, 1, None, None)
    room_list.append(room_0)
    room_1 = Room("You are in the south hallway.\nThere is a door to the west and east and an opening to the north.",
                  4, 2, None, 0)
    room_list.append(room_1)
    room_2 = Room("You are in the dining room.\nThere is a door to the west.", None, None, None, 1)
    room_list.append(room_2)
    room_3 = Room("You are in the first bedroom.\nThere is a door to the east.", None, 4, None, None)
    room_list.append(room_3)
    room_4 = Room("You are in the north hallway.\nThere is a door to the west and east and an opening to the south.",
                  6, 5, 1, 3)
    room_list.append(room_4)
    room_5 = Room("You are in the kitchen.\nThere is a door to the west.", None, None, None, 4)
    room_list.append(room_5)
    room_6 = Room("You are in the balcony.\nThere is a door to the south.", None, None, 4, None)
    room_list.append(room_6)
    Done = False

    while Done is False:
        # while the program is not finish do this code
        print(room_list[current_room].description)
        print("")
        # prompts the user a question to which they respond with a direction
        user_input = input("What is your direction? (Enter in letters or full direction name): ")

        print("")

        # user picks to move north
        if user_input.upper() == "N" or user_input.upper() == "NORTH" or user_input == "NoRtH":
            next_room = room_list[current_room].north
            print("")
            # if next_room is None, you can't move that direction
            if next_room is None:
                print("You can't move north.")
            # if there is a room to move to in that direction, you can move that direction
            elif next_room == room_list[current_room].north:
                print("You moved to the north.")
                current_room = next_room

        # user picks to move east
        elif user_input.upper() == "E" or user_input.upper() == "EAST" or user_input == "EaSt":
            next_room = room_list[current_room].east
            # if next_room is None, you can't move that direction
            if next_room is None:
                print("You can't move east.")
            elif next_room == room_list[current_room].east:
                print("You moved to the east.")
                current_room = next_room

        # user picks to move south
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH" or user_input == "SoUtH":
            next_room = room_list[current_room].south
            # if next_room is None, you can't move that direction
            if next_room is None:
                print("You can't move south.")
            elif next_room == room_list[current_room].south:
                print("You moved to the south.")
                current_room = next_room

        # user picks to move west
        elif user_input.upper() == "W" or user_input.upper() == "WEST" or user_input == "WeSt":
            next_room = room_list[current_room].west
            # if next_room is None, you can't move that direction
            if next_room is None:
                print("You can't move west.")
            elif next_room == room_list[current_room].west:
                print("You moved to the west.")
                current_room = next_room

        # quit
        elif user_input.upper() == "Q" or user_input.upper() == "Quit" or user_input == "QuIt":
            print("\nQuiting game.")
            exit()

        # any other input is invalid
        else:
            print("\nInvalid input!")


main()
