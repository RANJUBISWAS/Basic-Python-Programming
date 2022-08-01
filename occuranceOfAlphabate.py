#find occurance of each alphabate in a given string
k =  "abcabcabcsd"
d ={}
for i in k:
  if i in d.keys():
    d[i] += 1
  else:
    d[i] = 1

print(d)
