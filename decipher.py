# COMP 340
# Amari Sisco

def decipher(babyExp):
    srcCode = ""
    indexCounter = 0

    for i in range(len(babyExp)):
        if indexCounter < len(babyExp):
            if babyExp[indexCounter] == "p":
                if isWord("pee", indexCounter, babyExp):
                    indexCounter += 2
                    srcCode += "+"
            if babyExp[indexCounter] == "g":
                if isWord("gah", indexCounter, babyExp):
                    indexCounter += 2
                    srcCode += "-"
            if babyExp[indexCounter] == "h":
                if isWord("heh", indexCounter, babyExp):
                    indexCounter += 2
                    srcCode += "/"
            if babyExp[indexCounter] == "m":
                if isWord("milk", indexCounter, babyExp):
                    indexCounter += 3
                    srcCode += "*"
                elif isWord("mama", indexCounter, babyExp):
                    indexCounter += 3
                    srcCode += "("
            if babyExp[indexCounter] == "d":
                if isWord("dada", indexCounter, babyExp):
                    indexCounter += 3
                    srcCode += ")"
            if babyExp[indexCounter] == "b":
                aCount = 0
                if len(babyExp) > 1:
                    for x in range(9):
                        if indexCounter < len(babyExp) - 1:
                            if babyExp[indexCounter + 1] == "a":
                                aCount += 1
                                indexCounter += 1
                            elif aCount == 9:
                                srcCode += "9"
                                break
                    if indexCounter != len(babyExp) - 1:
                        srcCode += str(aCount)
                    else:
                        srcCode += str(aCount)
                        break
                else:
                    srcCode += "0"

            if indexCounter != len(babyExp) - 1:
                indexCounter += 1

    return srcCode


def isWord(desiredWord, currIndex, srcCode):
    # going to gather the letters after the current index to see if they are the same as the desired word
    testingWord = ""
    for i in range(len(desiredWord)):
        if currIndex != len(srcCode):
            testingWord += srcCode[currIndex]
            currIndex += 1
        if testingWord == desiredWord:
            return True
    return False
