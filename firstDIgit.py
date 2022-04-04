num = int(input("Enter Number:"))
while(num > 0):
    firstDigit = num % 10
    num //= 10
print(firstDigit)
