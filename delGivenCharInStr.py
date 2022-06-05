# delete all occurrences of a specified character in a given string.
inputStr = "This is a test string.If the test pass.It will return a string without duplicate word."
ch = 't'
def Function(str,ch):
    str = str.lower().replace(ch, "")
    return str
test = Function(inputStr,ch)
print(test)
