# COMP 340
# Amari Sisco


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


def tokenize(srcCode):
    tokSeq = []
    while srcCode != "":
        char = srcCode[0]
        if char == "+":
            newToken = Token("PLUS", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == "-":
            # checks to see if the "-" is not the first char in the given sequence
            if tokSeq:
                # checks if the character before "-" was a number if not then it means it is a negative and
                # we replace the "-" with (0 - 1) * because this is a readable function to the parser
                if tokSeq[-1].type != "NUMBER":
                    tokSeq.append(Token("LPAREN", "("))
                    tokSeq.append(Token("NUMBER", "0"))
                    tokSeq.append(Token("MINUS", "-"))
                    tokSeq.append(Token("NUMBER", "1"))
                    tokSeq.append(Token("RPAREN", ")"))
                    tokSeq.append(Token("MULTIPLICATION", "*"))
                    srcCode = srcCode[1:]
                # if the character before the "-" is a number than it is treated as a minus
                else:
                    newToken = Token("MINUS", char)
                    tokSeq.append(newToken)
                    srcCode = srcCode[1:]
            # if the "-" is the first character in a given sequence then it is treated as a negative and replaced with
            # (0 - 1) * because this is a readable function to the parser
            else:
                tokSeq.append(Token("LPAREN", "("))
                tokSeq.append(Token("NUMBER", "0"))
                tokSeq.append(Token("MINUS", "-"))
                tokSeq.append(Token("NUMBER", "1"))
                tokSeq.append(Token("RPAREN", ")"))
                tokSeq.append(Token("MULTIPLICATION", "*"))
                srcCode = srcCode[1:]

        elif char == "/":
            newToken = Token("DIVISION", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == "(":
            newToken = Token("LPAREN", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == ")":
            newToken = Token("RPAREN", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == "*":
            newToken = Token("MULTIPLICATION", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]

        elif char == " ":
            srcCode = srcCode[1:]

        elif char.isdigit():
            numbStr = ""
            while char.isdigit():
                numbStr += char
                srcCode = srcCode[1:]
                if srcCode == "":
                    char = ""
                else:
                    char = srcCode[0]
            newToken = Token("NUMBER", numbStr)
            tokSeq.append(newToken)

    return tokSeq


# def replaceNegative(tokSeq):
#     newToqSeq = []
#     for i in range(len(tokSeq)):
#         if tokSeq[i].type == "NEGATIVE":
#             newToqSeq.append(Token("LPAREN", "("))
#             newToqSeq.append(Token("NUMBER", "0"))
#             newToqSeq.append(Token("MINUS", "-"))
#             newToqSeq.append(Token("NUMBER", "1"))
#             newToqSeq.append(Token("MULTIPLICATION", "*"))
#     return newToqSeq
