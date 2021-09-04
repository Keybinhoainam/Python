test=int(input())
for t in range(test):
    n=int(input())
    a=[]
    for i in range(n):
        tmp1=int(input())
        a.append(tmp1)
    a.sort()
    # print(a)
    kq=0
    dem=0
    i=0
    while(i<n):
        tmp=a.count(a[i])
        # print(tmp,dem,a[i])
        if(dem<tmp):
            dem=tmp
            kq=a[i]
        i+=tmp
    print(kq)
