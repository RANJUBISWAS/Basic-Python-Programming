num = int(input("Enter Number:"))
li = list() #or "li = []"
for i in range(2, num//2+1): #factor of a number cann't be greater than half of the original number
    if(num % i == 0):
        prime = 1 #this variable will be modified,if the factor is not a prime factor
        for j in range(2,i//2+1):#for i==2,'for loop' won't run
            if(i % j == 0):
                prime = 0
                break
        if(prime == 1):li.append(i)
print(li)
