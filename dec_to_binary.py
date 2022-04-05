#using 'bin()' function
num = int(input("Enter Number:"))
print(bin(num)) #pefix of the output will be "0b"

#recuirsive method(solution of the prefix problem)

num = int(input("Enter Number:"))
def decToBin(num):
    if num> 1:
        decToBin(num//2)
    print(num % 2, end='')
decToBin(num)
