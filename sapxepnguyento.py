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
n=int(input())
a=[int(x) for x in input().split()]
snt=[]
kt(snt)
b=[]
for i in range(n):
    if(a[i] in snt):
        b.append(a[i])
        a[i]=-1
b.sort()
j=0
for i in a:
    if(i==-1):
        print(b[j],end=' ')
        j+=1
    else: print(i,end=' ')