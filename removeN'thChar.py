#Python program to remove the n'th 
# index character from a nonempty string.
inputStr = "akfjljfldksgnlfskgjlsjf"
n = 5

def abc(inputStr, n):
    if n > len(inputStr):
        print("invalid 'n'.")
        return 0 
    return inputStr[0:n-1] + inputStr[n:]

newStr = abc(inputStr,n)
print(newStr)
