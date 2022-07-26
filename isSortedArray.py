#recursivly check if an array is sorted or not

arr = [1,2,3,4,5,6,7,8,9]
#different test case
# arr = [1,2,3,99999,5,6,7,8,9]
# arr = []
size = len(arr)

def check(arr,size):
  if arr == [] or size == 1:
    return True
  if arr[0] > arr[1]:
    return False
  else:
    first, *rest = arr
    smaller = check(rest,size-1)
    return smaller  

result = True if check(arr,size) == True else False
print(result)
