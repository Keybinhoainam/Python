test=int(input())
for t in range(test):
    s=input()
    i=1
    for i in range(1,len(s)):
        if(s[i-1]>s[i]):break
    if(i==len(s)-1):print("YES")
    else:print("NO")