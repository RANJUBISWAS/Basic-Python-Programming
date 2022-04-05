num = int(input("Till how many number do you want to find Prime numbers:"))
li = []
if num < 2:
    print("No prime number")
else:
    for i in range(2, num+1):
        prime =1
        for j in range (2, i//2+1):
            if i % j == 0:
                prime = 0
                break
        if prime == 1:
            li.append(i)
print(li) 
