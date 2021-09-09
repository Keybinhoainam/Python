def kt(snt):
    n=10000
    check=[0]*10005
    for i in range(2,n+1):
        if(check[i]==0):
            snt.append(i)
            j=i*i
            while(j<=n):
                check[j]=1

                j+=i

snt=[]
kt(snt)
n,m=map(int,input().split())
a=[]
for i in range(n):
    b=[int(x) for x in input().split()]
    a.append(b)

maxnt=-1
for i in range(n):
    for j in range(m):
        if(a[i][j] in snt and a[i][j]>maxnt):
            maxnt=a[i][j]
if(maxnt==-1):print("NOT FOUND")
else:
    print(maxnt)
    for i in range(n):
        for j in range(m):
            if(a[i][j]==maxnt):
                print(f"Vi tri [{i}][{j}]")
