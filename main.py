# COMP 340
# Amari Sisco
import lexer
import parserr
import evaluator

while True:
    srcCode = input(">>> ")
    if srcCode == "poopoo":
        break
    tokSeq = lexer.tokenize(srcCode)
    rootNode = parserr.parse(tokSeq)
    result = evaluator.evaluate(rootNode)
    print("The Result is: ", result)
print("Now it is tim to go poo poo")