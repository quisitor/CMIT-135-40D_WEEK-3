"""

:Student: Craig Smith
:Week-3: Conditional Logic Programs
:Module: grade_converter
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles

Purpose
-------
This module takes in a grade percentage from the user and converts it to a
letter grade based on a specific grading scale.

Constraints
-----------
1. Prompt the user to enter a grade percentage
2. Use the grading scale listed below

Parameters
----------
:grade_percentage: Number input by user at the terminal
:GRADING_SCALE: Dictionary mapping Letter Grade to Percentage
:returns: Letter grade equivalent of the user entered percentage

GRADING SCALE
-------------
=====   =====
Grade	Range
=====   =====
A+      >= 99
A	    93
A-	    90-92
B+	    87-89
B	    83-86
B-	    80-82
C+	    77-79
C	    73-76
C-	    70-72
D+	    67-69
D	    63-66
D-	    60-62
F	    < 60
=====   =====

"""

# Constants


GRADING_SCALE = {
    'A+': [99, 100],
    'A': [93, 94, 95, 96, 97, 98],
    'A-': [90, 91, 92],
    'B+': [87, 88, 89],
    'B': [83, 84, 85, 86],
    'B-': [80, 81, 82],
    'C+': [77, 78, 79],
    'C': [73, 74, 75, 76],
    'C-': [70, 71, 72],
    'D+': [67, 68, 69],
    'D': [63, 64, 65, 66],
    'D-': [60, 61, 62],
    'F': [num for num in range(0, 60)]
}

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


# Main

if __name__ == '__main__':
    grade_percentage = input("Please enter your grade percentage: ")
    percentage_as_num = convert_str_to_num(grade_percentage)
    letter_grade = ""

    # Handle user values that our out of grading scale range
    if percentage_as_num < 0:
        percentage_as_num = 0
    elif percentage_as_num > 100:
        percentage_as_num = 100

    # Obtain letter grade associated with the percentage value
    for key, value in GRADING_SCALE.items():
        if int(percentage_as_num) in GRADING_SCALE[key]:
            letter_grade = key

    print(f"Your letter grade is a {letter_grade}.")
