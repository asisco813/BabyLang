# COMP 340
# Amari Sisco
def evaluate(rootNode):
    if rootNode.lChild == None and rootNode.rChild == None:
        return int(rootNode.value)
    else:
        result = 0
        leftResult = evaluate(rootNode.lChild)
        rightResult = evaluate(rootNode.rChild)
        # this if checks the current token in the rootNode to identify what the function is and executes based on that
        if rootNode.type == "PLUS":
            result = leftResult + rightResult
        # Code below derived from professor Paul Kim's work above
        elif rootNode.type == "MINUS":
            result = leftResult - rightResult
        elif rootNode.type == "MULTIPLICATION":
            result = leftResult * rightResult
        elif rootNode.type == "DIVISION":
            result = leftResult / rightResult
        return result
