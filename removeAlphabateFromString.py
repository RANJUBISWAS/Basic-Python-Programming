# remove a alphabate from a given string

inputStr = "asdfghasdfgasdfgaafghj"
removeAlphabate = 'a'

def remove(inputStr, removeAlphabate):
  if inputStr == '':
    return ''
  else:
    head = inputStr[0]
    if head == removeAlphabate:
      return remove(inputStr[1:],removeAlphabate)
    else:
      return head + remove(inputStr[1:] , removeAlphabate)

result = remove(inputStr, removeAlphabate)
print(result)
