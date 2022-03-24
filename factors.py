f =list()
n = int(input("Number:"))
i = 1
while(n > 0 and i <= n):
    if(n % i == 0):
        f.append(i)
    i += 1
print(f)
