"""Pig latin is when you take an english word that begins with a consonant,
move the constant to the end, and then add ay to the end of the word. This
Program will take in a word as an input and produce its pig latin counterpart"""


def main():
    """Take a word input and change it into pig latin"""

    # Assign the inputted word to a variable
    word = input('Please enter the word for translation: ')

    # Define a list of vowels
    vowels = ['a', 'e', 'i', 'o' 'u']

    # Determine if the first letter is a vowel or a consonant
    if word[0] in vowels:
        # If the first letter is a vowel, pig latin convention is to add 'way'
        # at the end of word
        pig_latin = f"{word}way"

    else:
        # If consonant, move the consonant to the end and add 'ay' to the end
        pig_latin = f"{word[1:]}{word[0]}ay"

    print(pig_latin)


if __name__ == "__main__":
    main()
