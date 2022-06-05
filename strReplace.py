# get a string from a given string where all
# occurrences of its first char have been changed
# to '$', except the first char itself.

inputStr = " Hello There"
def Function(inputStr):
    inputStr = inputStr.lower().strip()
    firstChar = inputStr[0:1]
    allOtherChar = inputStr[1:]
    allOtherChar = allOtherChar.replace(firstChar, '$')
    newStr = firstChar + allOtherChar
    return newStr

test = Function(inputStr)
print(test)
