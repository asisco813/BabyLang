# COMP 340
# Amari Sisco
class TreeNode:
    def __init__(self, type, value, precedence):
        self.type = type
        self.value = value
        self.precedence = precedence

    parent = None
    lChild = None
    rChild = None


def getPrecedence(type):
    precedence = 0
    if type == "PLUS" or type == "MINUS":
        precedence = 1
    elif type == "MULTIPLICATION" or type == "DIVISION":
        precedence = 2
    return precedence


def createTreeNodeList(tokSeq):
    treeNodeList = []
    x = 0
    for token in tokSeq:
        if token.type == "LPAREN":
            x += 4
        elif token.type == "RPAREN":
            x -= 4
        if token.type != "LPAREN" and token.type != "RPAREN":
            newNode = TreeNode(token.type, token.value, getPrecedence(token.type) + x)
            treeNodeList.append(newNode)
    return treeNodeList


def parse(tokSeq):
    rootNode = None
    treeNodeList = createTreeNodeList(tokSeq)
    parsing(treeNodeList)
    rootNode = findRoot(treeNodeList)
    return rootNode


def findRoot(treeNodeList):
    rootNode = None
    for node in treeNodeList:
        if node.parent == None and node.type != "DUMMY":
            rootNode = node
            break
    return rootNode


def parsing(treeNodeList):
    if len(treeNodeList) == 1:
        return treeNodeList
    dummyNode = TreeNode("DUMMY", "", 0)
    treeNodeList.insert(0, dummyNode)
    treeNodeList.append(dummyNode)
    for index in range(len(treeNodeList)):
        node = treeNodeList[index]
        if node.type == "NUMBER":
            lOp = treeNodeList[index - 1]
            rOp = treeNodeList[index + 1]
            if rOp.precedence > lOp.precedence:
                # right
                rOp.lChild = node
                node.parent = rOp
                if lOp.type != "DUMMY":
                    lOp.rChild = rOp
                    rOp.parent = lOp
            else:
                # left
                lOp.rChild = node
                node.parent = lOp
                if rOp.type != "DUMMY":
                    # find proper position of rOp
                    while lOp.parent != None:
                        if lOp.parent.precedence < rOp.precedence:
                            break
                        lOp = lOp.parent
                    if lOp.parent != None:
                        lOp.parent.rChild = rOp
                        rOp.parent = lOp.parent
                    rOp.lChild = lOp
                    lOp.parent = rOp


def printTree(rootNode):
    if rootNode.lChild == None and rootNode.rChild == None:
        print(rootNode.value, end="")
    else:
        print("(", end="")
        printTree(rootNode.lChild)
        print(rootNode.value, end="")
        printTree(rootNode.rChild)
        print(")", end="")
