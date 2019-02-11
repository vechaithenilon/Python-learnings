""" Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password security check module. The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results."""

# My Code
def checkio(data: str) -> bool:
    # replace this for solution

    check_status1 = False

    check_status2 = False

    check_status3 = False

    check_status4 = False

    # check num of letters

    if len(data) >= 10:
        check_status1 = True

    import string

    lower_letters = set(string.ascii_lowercase)

    num_lower = 0

    upper_letters = set(string.ascii_uppercase)

    num_upper = 0

    num = 0

    # check lower letters

    for i in data:

        if i in lower_letters:

            num_lower += 1

        elif i in upper_letters:

            num_upper += 1

        elif i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:

            num += 1

    if num_lower >= 1:
        check_status2 = True

    if num_upper >= 1:
        check_status3 = True

    if num >= 1:
        check_status4 = True

    if check_status1 and check_status2 and check_status3 and check_status4 is True:

        return True

    else:

        return False




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert checkio('A1213pokl') == False, "1st example"

    assert checkio('bAse730onE4') == True, "2nd example"

    assert checkio('asasasasasasasaas') == False, "3rd example"

    assert checkio('QWERTYqwerty') == False, "4th example"

    assert checkio('123456123456') == False, "5th example"

    assert checkio('QwErTy911poqqqq') == True, "6th example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")



# Best code I can find online
import re
# \d is shorthand for [0-9]
DIGIT_RE = re.compile('\d')
# How to quickly combine a check alphabet list
UPPER_CASE_RE = re.compile('[A-Z]')

LOWER_CASE_RE = re.compile('[a-z]')


def checkio(data):
    """

    Return True if password strong and False if not



    A password is strong if it contains at least 10 symbols,

    and one digit, one upper case and one lower case letter.

    """
    # Clean check method if not (think of the opposite set) if not wrong at all --> True
    if len(data) < 10:
        return False

    if not DIGIT_RE.search(data):
        return False

    if not UPPER_CASE_RE.search(data):
        return False

    if not LOWER_CASE_RE.search(data):
        return False

    return True


if __name__ == '__main__':
    assert checkio('A1213pokl') == False, 'First'

    assert checkio('bAse730onE4') == True, 'Second'

    assert checkio('asasasasasasasaas') == False, 'Third'

    assert checkio('QWERTYqwerty') == False, 'Fourth'

    assert checkio('123456123456') == False, 'Fifth'

    assert checkio('QwErTy911poqqqq') == True, 'Sixth'

    print('All ok')



"""Code part"""

import re

digit_check = re.compile("\d")
upper_check = re.compile("[A-Z]")
lower_check = re.compile("[a-z]")

def checkio(data: str) -> bool:

    if len(data) < 10:
        return False

    if not digit_check.search(data):
        return False
    if not upper_check.search(data):
        return False
    if not lower_check.search(data):
        return False

    return True


"""test part"""
if __name__ == '__main__':

    assert checkio('A1213pokl')==False, 'First'

    assert checkio('bAse730onE4')==True, 'Second'

    assert checkio('asasasasasasasaas')==False, 'Third'

    assert checkio('QWERTYqwerty')==False, 'Fourth'

    assert checkio('123456123456')==False, 'Fifth'

    assert checkio('QwErTy911poqqqq')==True, 'Sixth'

    print('All ok')

# Learning point "" equals ''
# Learning point: practice if not then if
# Learning point: how to use re module from python