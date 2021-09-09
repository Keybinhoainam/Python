n,m=map(int ,input().split())
a=[]
for i in range(n):
    b=[int(x) for x in input().split()]
    a.append(b)
if(n==m):
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=" ")
        print()
elif(n>m):
    dem=n-m
    for i in range(n):
        if(i%2==0 and dem>0):
            dem-=1
            continue
        else:
            for j in range(m):
                print(a[i][j],end=" ")
            print()
else:
    tmp=[]
    dem=m-n
    i=1
    while(dem>0):
        dem-=1
        tmp.append(i)
        i+=2

    for i in range(n):
        for j in range(m):
            if(j not in tmp):print(a[i][j],end=" ")
        print()