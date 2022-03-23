def perfect_squre(x):
    i = 1
    while (i**2 <= x):
        if ((x % i == 0) and (x / i == i)):
            return True
        i += 1
    return False
x = int(input("Enter no:"))
if(perfect_squre(x)):
    print("True")
else: print("False")
