"""

:Student: Craig Smith
:Week-3: Conditional Logic Programs
:Module: voting_test
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles

Purpose
-------
This module takes in a potential voter's age and determines if they are 18 or
older and able to legally vote.

Constraints
-----------
1. Prompt the user to enter their age
2. Output uses the one of the following
    a. 'You must be 18 to vote.'
    b. 'You are of voting age.'

Parameters
----------
:param age: user input - integer
:returns:  answer if age qualifies person to vote - string

"""

if __name__ == '__main__':
    age_input = input("Please enter your age in years: ")

    while True:
        try:
            age = int(age_input)
            break;
        except ValueError:
            age_input = input("Please enter your age in years: ")

    if age >= 18:
        print("You are of voting age.")
    else:
        print("You must be 18 to vote.")
