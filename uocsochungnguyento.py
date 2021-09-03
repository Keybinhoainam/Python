import math
def ucln(a,b):
    if(b==0):return a
    return ucln(b,a%b)
def snt(n):
    if(n==1 or n==0):return 0
    tmp=int(math.sqrt(n))
    # print(n,tmp,math.sqrt(n))
    for i in range(2,tmp+1):
        if(n%i==0):return 0
    return 1

test=int(input())
for t in range(test):
    a,b=map(int,input().split())
    uoc=ucln(a,b)
    # print(uoc)
    tmp=0
    while(uoc>0):
        tmp=tmp+(uoc%10)
        uoc=int(uoc/10)
    # print(tmp)
    if(snt(tmp)==1):print("YES")
    else:print("NO")
