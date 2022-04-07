s = "abcdcbea" #enter string here
pal = 1
for i in range(0 , len(s)//2):
    if s[i] != s[-(i+1)]:
        pal = 0
if pal == 1:print("pal")
else:print("not pal")
