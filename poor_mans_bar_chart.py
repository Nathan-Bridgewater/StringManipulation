"""This program takes a sentence as an input and returns a 'Bar chart'
in a terminal window of the amount of individual letters"""
from collections import defaultdict
import pprint


def main():
    """Take a string input and form a bar chart from it"""

    # Assign the sentence to variable
    sentence = input('Please enter a sentence: ')

    # define a list containing all of the letters in the alphabet
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Define a dictionary which provides a default value of a list
    # for a non existent key
    dictionary = defaultdict(list)

    # Loop through each character in the sentence
    for letter in sentence:
        letter = letter.lower()

        if letter in letters:
            # The list returned is appended with the letter from the sentence
            dictionary[letter].append(letter)

    # pprint module displays the dictionary in the format of a bar chart
    pprint.pprint(dictionary, width=200)


if __name__ == "__main__":
    main()
