import re
def kt(s):
    if((ord(s)>=ord('0') and ord(s)<=ord('9')) or (ord(s)>=ord('a') and ord(s)<=ord('z'))):
        return 1
    return 0
def cmp(n):
    return a.values()

n=int(input())
a=dict()
for t in range(n):
    s = input()
    s = re.sub(r"[^a-zA-Z]"," ",s)
    s = s.lower().split()
    for i in s:
        if(i in a):a[i]+=1
        else:a[i]=1
a=dict(sorted(a.items(),key=lambda x:x[0]))
for i in sorted(a.items(),key=lambda x:x[1],reverse=True):
    print(i[0],i[1])
