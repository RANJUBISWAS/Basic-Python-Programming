# remove duplicate words from a given string.
inputStr = "This is a test string.If the test pass.It will return a string without duplicate word."
def Function(str):
    str = str.split(' ')
    newStr = ""
    for word in str:
        if word not in newStr or word == '.' :
            newStr = newStr +" "+ word
    newStr = newStr.strip()
    return newStr
test = Function(inputStr)
print(test)
