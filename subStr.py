# get a string made of the first 2 
# and the last 2 chars from a given 
# a string. If the string length is less 
# than 2, return instead of the empty string.

inputStr = " hello there! "
def tempFunction(inputStr):
    inputStr = inputStr.strip()
    strLen = len(inputStr)
    str = ""
    if strLen < 2:
        return str
    else:
        newStr = inputStr[0:2]+inputStr[strLen-2:]
        return newStr
test = tempFunction(inputStr)
print(test)
