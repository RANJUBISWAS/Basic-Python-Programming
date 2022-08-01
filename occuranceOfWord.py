#find occurance of each word in a given string

k =  "ab abc aabc abab abc ab aaa"
k = k.split(' ')

d ={}
for i in k:
  if i in d.keys():
    d[i] += 1
  else:
    d[i] = 1

print(d)
