# COMP 340
# Amari Sisco
import lexer
import parserr
import evaluator
import decipher

while True:
    babyExp = input(">>> ")
    if babyExp == "poopoo":
        break
    srcCode = decipher.decipher(babyExp)
    tokSeq = lexer.tokenize(srcCode)
    rootNode = parserr.parse(tokSeq)
    result = evaluator.evaluate(rootNode)
    print("The Result is: ", result)

print("Now it is tim to go poo poo")
