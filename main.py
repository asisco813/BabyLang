#COMP 340 HW5
#Amari Sisco

import lexer

srcCode = "(3*43) + 100 / 3"
tokSeq = lexer.tokenize(srcCode)

for i in tokSeq:
    print(i.type, i.value)