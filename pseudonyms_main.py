"""Create goofy names by randomly combining names from two seperate lists."""
import sys
import random


def main():
    """Choose names from the two lists, combine and print them"""

    # Print a welcome message for the program
    print("Welcome to the random name generator. \n")

    # Define a tuple containing goofy first names to be used
    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
             'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
             'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Hucklebe',
             'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
             'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mtroid',
             '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
             'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
             'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
             "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
             'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
             'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
             "Winston 'Jazz Hands'", 'Worms')

    # Define a tuple containing goofy last names to be used
    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goensmith',
            'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
            'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
            'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nles',
            'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
            'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
            'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
            'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
            'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
            'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
            'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')

    # Start the main program loop, this runs until a "break" is issued
    while True:
        # Use the choice method from random to pick a name from each tuple
        # and assign the names to a variable
        first_name = random.choice(first)
        second_name = random.choice(last)

        # Print the neatly formatted first and second name in red
        print(f"Hi {first_name.title()} {second_name.title()}", file=sys.stderr)

        # Allow the user to input if they want to play again
        try_again = input('Press enter to continue or q to quit: ')

        # a user input of 'q' or 'Q' ends the loop
        if try_again.lower() == 'q':
            break

    # pressing enter doesn't assign a return value for input so cmd closes
    input('Press enter to quit the program')


if __name__ == "__main__":
    main()
