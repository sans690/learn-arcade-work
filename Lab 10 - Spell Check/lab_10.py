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
# for words in file
for item in dictionary_file:
    # takes out space
    words = item.strip().upper()
    # list adds the file from variable
    dictionary_list.append(words)
# closes the file
dictionary_file.close()
# print(dictionary_list)


print("--- Linear Search ---")


def linear_search():
    # opens and reads file, then closes it
    alice_file = open("AliceInWonderLand200.txt")
    # for the lines in the file
    for lines in alice_file:
        # variable holds the value of split lines from file
        line_list = split_line(lines)
        # for words in list
        for words in line_list:
            # current position
            i = 0
            # while current position is less than the length of list and words are not equal to the value in the
            # list position
            while i < len(dictionary_list) and dictionary_list[i] != words.upper():
                # add one to the current position
                i += 1
            # breaks out the code when condition fails
            # if word is not found
            if words != dictionary_list:
                print("possible misspelled word:", words)
    alice_file.close()
linear_search()