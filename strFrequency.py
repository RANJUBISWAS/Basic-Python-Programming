#Following code will only work on single line string
inputStr = "Hello World"
inputStr = inputStr.lower()
print(inputStr)
uniqueAlphabate = []
frequency = []
for alphabate in inputStr:
    if alphabate != " " and alphabate not in uniqueAlphabate:
        uniqueAlphabate.append(alphabate)
        frequency.append(1)
    elif alphabate == " ":
        pass
    else:
        index = uniqueAlphabate.index(alphabate)
        frequency[index] += 1
length = len(uniqueAlphabate)
print("Frequency of each alphabate:")
for i in range(length):
    print(uniqueAlphabate[i],"=",frequency[i])
