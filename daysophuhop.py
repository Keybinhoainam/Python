test=int(input())
for t in range(test):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    a.sort()
    b.sort()
    i=0
    for i in range(n):
        if(a[i]>b[i]):break
    if(i==n-1):print("YES")
    else: print("NO")