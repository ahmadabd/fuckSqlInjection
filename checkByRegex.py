## check user input when you now correct input form
## in this code user input a code by maximum len == 4

import re

def checkInput(code):
    if re.search("^[0-9]{4}$", code):
        return True
    else:
        return False
