num = int(input("Enter Number:"))
base = 2 #to convert from any other number system to decimal,
         #change this variable to the base of the number system
digit = 0 
temp = num
dec = 0
while(temp):
    digit += 1
    temp //= 10
for i in range(0 , digit):
    dec += ((num%10)*(base**i))
    num //=10
print(dec)
