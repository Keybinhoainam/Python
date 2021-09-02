import array as arr


test=int(input())
for t in range(test):
    n=int(input())
    # for i in range(n):
    a=[int(x) for x in input().split()]
    a.sort()
    tmp=1
    m=1
    stt=0
    for i in range(1,n):
        if(a[i]==a[i-1]):
            tmp+=1
        else: tmp=1
        if(tmp>m):
            m=tmp
            stt=i
    if(m>n/2):print(a[stt])
    else: print("NO")