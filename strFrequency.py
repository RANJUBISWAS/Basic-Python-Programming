#Following code will only work on single line string.
#Though it does work.Still the procedure is not satisfactory.
inputStr = "Hello World"
inputStr = inputStr.lower()
print(inputStr)
uniqueAlphabate = []
frequency = []
for alphabate in inputStr:
    if alphabate != " " and alphabate not in uniqueAlphabate: #if you want whitespace to be counted,just write -> "if aplhabate not in uniqueAlphabate"
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
 
#----------------------------------------------------------------
#a better way to do it will be:(following code will ignore all whitespace,tab and new line)

import string
def strFrequency (inputStr):
  inputStr = inputStr.translate(str.maketrans('','',string.whitespace))
  tempDict = {}
  for alphabate in inputStr:
    if alphabate not in tempDict:
      tempDict[alphabate] = 1
    else: 
      tempDict[alphabate] += 1
  return tempDict

testStr = strFrequency("""h   i 
there!""")
print(testStr)
