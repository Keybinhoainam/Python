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
a.sort()
j=0
kq=0
for i in a:
    if(i not in snt):
        if(i>2):
            while(snt[j]<i):j+=1
            tmp=min(snt[j]-i,i-snt[j-1])
            kq=max(tmp,kq)
        else:
            kq=max(kq,2-i)
print(kq)


