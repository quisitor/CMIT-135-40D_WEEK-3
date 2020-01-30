"""

:Student: Craig Smith
:Week-3: Conditional Logic Programs
:Module: guess_the_number
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles

Purpose
-------
The computer chooses a random number between 0 and 9 and the user has to guess
the randomly generated number.

Constraints
-----------
1. Random number between 0 and 9, inclusive
2. Import and use the randint method from the random module

:param guessed_input: Number input by user at the terminal

:output responses: 'Guess Higher', 'Guess Lower', 'Great job! You guessed the correct number: '

"""

# Imports
from random import randint

# Helper Functions


def convert_str_to_num(str_number):
    """
    This function takes a string, validates it can be converted to a number
    and returns either a string or float representation of the string.

    :param str_number: a string representation of a number
                       ex: "123", "123.3", "-123", "-123.3"

    :return: an int or float representing the number in the string

    """

    while True:
        if str_number.replace('-', '', 1).isnumeric():
            return int(str_number)
        elif str_number.replace('-', '', 1).replace('.', '', 1).isnumeric():
            return float(str_number)
        else:
            str_number = input('Please enter a valid number: ')


def lower_higher(answer, guess):
    """
    This function takes a known number and an unknown number and compares the
    difference. The function will return a message indicating to the calling
    function whether or not the user needs to guess higher or lower than the
    number just guessed.

    :param answer: known integer value determined by the calling function
    :param guess: number passed in by the end user
    :return: 'Guess Higher', 'Guess Lower', True

    """

    if answer == guess:
        return True
    elif guess < answer:
        return 'Guess Higher'
    elif guess > answer:
        return 'Guess Lower'


# Main
random_number = randint(0, 9)
matching_value = False

guessed_input = input('The computer has chosen a number at random between 0 and 9.\n '
                      'Please try and guess the chosen number: ')

while not matching_value:
    guessed_number = convert_str_to_num(guessed_input)
    result = lower_higher(random_number, guessed_number)

    if result == 'Guess Higher':
        guessed_input = input('Guess a Higher Number: ')
    elif result == 'Guess Lower':
        guessed_input = input('Guess a Lower Number: ')
    else:
        matching_value = result

print('Great job! You guessed the correct number: ', random_number)
