## Remove sql command in lowerCase or upperCase from input.

class fuckSqlInjection:
    def __init__(self):
        self.badChars = ["select","union", "drop", ";", "--", "insert", "delete", "xp_", "#", "%", "&", \
            "'", "(", ")", "/", "\\", ":", ";", "<", ">", "=", "[", "]", "?", "`", "|", "<=", ">=", \
            "*", "as", "in", "between"]

    def checkVul(self, userInput):
        inp = userInput.split(" ")

        for char in self.badChars:
            if char in inp:
                inp.remove(char)
            if char.upper() in inp:
                inp.remove(char.upper())

        inp = " ".join(inp)

        return inp
