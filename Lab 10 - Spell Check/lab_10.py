import re


# This function takes in a line of text and returns
# a list of words in the line.
# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall("[A-Za-z]+(?:'[A-Za-z]+)?", line)


# creates a list
dictionary_list = []
# variable holds the open file
dictionary_file = open("dictionary.txt")
# for item in file
for item in dictionary_file:
    words = item.strip()
    # takes out space and uppercase
    # list adds the values(item) from the file
    dictionary_list.append(words)
    # closes the file
dictionary_file.close()
# print(dictionary_list)

def linear_search():

    # variable holds the open file
    alice_file = open("AliceInWonderLand200.txt")
    # for the lines in the file
    for lines in alice_file:
        # variable holds the value of split lines from file
        line_list = split_line(lines)
        # for word_list in list
        for word_list in line_list:
            # current position
            i = 0
            # while current position is less than the length of list and word_list is equal to the value in the
            # list position
            while i < len(dictionary_list) and word_list.upper() in dictionary_list[i]:
                # add one to the current position
                i += 1
                return i
            # breaks out the code when condition fails
            # if word_list in list
            if i < len(dictionary_list) and word_list.upper() not in dictionary_list[i]:
                print("possible misspelled word:", word_list)
    alice_file.close()
linear_search()

print("--- Binary Search ---")


def binary_search():

    lower_position = 0
    upper_position = len(dictionary_list) - 1
    word_found = False
    # loop until condition is met
    while lower_position <= upper_position:
        middle_pos = (lower_position + upper_position) // 2
        if dictionary_list[middle_pos] <
            lower_position = middle_pos + 1
        if dictionary_list[middle_pos] >
            upper_position = middle_pos - 1
        else:
            word_found = True
        if not word_found:
            print("possible misspelled word:",  )


binary_search()
