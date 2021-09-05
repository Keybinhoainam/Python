
test=int(input())
for i in range(test):
    s=input()
    n=len(s)
    check=0
    if(n%2==0 or s[0]==s[1]):check=1
    i=2
    while(i<n and check==0):
        if(s[i]!=s[i-2]):
            check=1
            break
        i+=2
    if(check==0):print("YES")
    else: print("NO")
