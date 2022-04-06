num = int(input("Enter Number:"))
li = []
pal = 1
while num > 0:
    li.append(num % 10)
    num //= 10
for i in range (0 , len(li)//2 +1):
    if li[i] != li[-(i+1)]:
        pal = 0
if pal == 1:
    print("Palindrome!")
else:print("Not Palindrome!")
