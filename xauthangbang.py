test=int(input())
for t in range(test):
    s=input()
    s1=s[::-1]
    check=1
    for i in range(len(s)-1):
        j=i+1
        a=ord(s[i])
        b=ord(s[j])
        c=ord(s1[i])     
        d=ord(s1[j])
        if(abs(a-b)!=abs(c-d)):
            check=0
            break
    if(check==1):print("YES")
    else: print("NO")