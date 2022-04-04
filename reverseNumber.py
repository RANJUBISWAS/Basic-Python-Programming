num = int(input("Enter Number:"))
revNum = 0
while(num > 0):
    temp = num % 10
    revNum = (revNum * 10) + temp
    num //=10 #if we use normal division instead of floor
print(revNum) #division,'num' might become float.so,result might become infinity.
