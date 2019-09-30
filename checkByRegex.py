## check user input when you now correct input form
## in this code user input a code by maximum len == 4

import re

def checkCode(code):
    if re.search("^[0-9]{4}$", code):
        return True
    else:
        return False


def checkPassword(password):
    if re.search("^[a-zA-Z0-9.$#]{4, 16}$", password):
        return True
    else:
        return False


def checkEmail(email):
    if re.search("^[a-zA-Z0-9]+\@[a-zA-Z0-9]+.[a-z]+$", email):
        return True
    else:
        return False
