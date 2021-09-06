test=int(input())
for t in range(test):
    n=int(input())
    a=[int(x) for x in input().split()]
    a.sort()
    i=0
    while(i<n):
        tmp=a.count(a[i])
        if(tmp%2!=0):
            kq=a[i]
            break
        i+=tmp
    print(kq)