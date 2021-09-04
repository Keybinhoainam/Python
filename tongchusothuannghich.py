def tongcs(n):
    tong=0
    i=len(n)-1
    while(i>=0):
        tong=tong + (ord(n[i])-ord('0'))
        i-=1
    return str(tong)

test=int(input())
for t in range(test):
    n=input()
    n1= tongcs(n)
    # n1="1221"
    a=list(n1)
    b=list(reversed(a))
    # print(a,b,sep="\n")
    check=0
    for i in range(len(a)):
        if(a[i]!=b[i]):
            check=1
            break
    if(check==0 and len(a)>1):print("YES")
    else: print("NO")