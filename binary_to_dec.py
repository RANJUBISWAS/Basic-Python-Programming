num = int(input("Enter Number:"))
digit = 0
temp = num
dec = 0
while(temp):
    digit += 1
    temp //= 10
for i in range(0 , digit):
    dec += ((num%10)*(2**i))
    num //=10
print(dec)
