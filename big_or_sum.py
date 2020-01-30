"""

:Student: Craig Smith
:Week-3: Conditional Logic Programs
:Module: big_or_sum
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles

Purpose
-------
This module takes in two user entered numbers and returns the sum of the two
numbers if they add up to less than 100 or a message indicating the sum is a big
number.

Constraints
-----------
1. Prompt the user to enter 2 numbers
2. If the sum of the numbers is <= 100, print 'They add up to ___.'
3. If the sum of the numbers i > 100, print 'They add up to a big number'

:param first_number: user input
:param second_number: user input

:terminal output: a message advising the sum is a big number or the number itself

"""


def convert_str_to_num(str_number):
    """
    This function takes a string, validates it can be converted to a number
    and returns either a string or float representation of the string.

    :param str_number: a string representation of a number
                       ex: "123", "123.3", "-123", "-123.3"

    :return: an int or float representing the number in the string

    """

    while True:
        if str_number.isnumeric():
            return int(str_number)
        elif str_number.replace('-', '', 1).isnumeric():
            return int(str_number)
        elif str_number.replace('.', '', 1).isnumeric():
            return float(str_number)
        elif str_number.replace('-', '', 1).replace('.', '', 1).isnumeric():
            return float(str_number)
        else:
            str_number = input('Please enter a valid number: ')


print('Enter two numbers at the prompts. '
      'You will receive a sum if they add up to < 101')
print()
first_number = convert_str_to_num(input('Please enter the first number: '))
second_number = convert_str_to_num(input('Please enter the second number: '))

print()
if first_number + second_number <= 100:
    print("\nThey add up to ", first_number + second_number)
else:
    print("\nThey add up to a big number.")
