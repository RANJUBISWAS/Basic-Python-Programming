# check whether any word in a given
# sting contains duplicate characrters
# or not. Return True or False.

inputStr = "quick brown fox jumps over the lazy dog" #enter input string here
def Function(inputStr):
    inputStr = inputStr.split(" ")
    for word in inputStr:
        for alphabate in word:
            count = word.count(alphabate)
            if count > 1:
                return True
    return False

test = Function(inputStr)
print(test)
