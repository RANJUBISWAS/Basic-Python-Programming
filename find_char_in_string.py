str = input("Enter string:")
li = ['@','#','$'] #add all those 'char' we want to find in string
for i in str:
    if i in li:
        print("found")
        break
    
