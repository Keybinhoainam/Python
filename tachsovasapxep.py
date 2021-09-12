import re
n=int(input())
a=[]
for t in range(n):
    s=input()
    s=re.sub(r"[^0-9]"," ",s)
    s=s.split()
    for i in s:
        a.append(int(i))
a.sort()
for i in a:
    print(i)

