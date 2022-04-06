num = int(input("Enter Number:"))
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * fact(n-1))
def factSum(num):
    fsum = 0
    while num > 0:
        fsum = fsum + fact(num % 10)
        num //= 10
    return fsum
if (factSum(num) == num):
    print("Strong Number!!!")
else: print("Not Strong Number!!!")
