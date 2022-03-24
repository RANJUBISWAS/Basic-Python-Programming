#using "math" module
from math import factorial
n = int(input("Number:"))
print(factorial(n))

#using recursion
n = int(input("Number:"))
def fact(n):
    if(n > 0):
        return (n*fact(n-1))
    else: return 1
print(fact(n))
