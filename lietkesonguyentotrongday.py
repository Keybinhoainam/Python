import math
tmp1=1000000
tmp2=math.sqrt(tmp1)
snt=[0]*(tmp1+5)
snt[1]=snt[0]=1
for i in range(2,tmp1+1):
    if(snt[i]==0):
        j=i*i
        while(j<=tmp1):
            snt[j]=1
            j+=i


n=int(input())
a=[int(x) for x in input().split()]
check=[0]*(tmp1+5)
for i in a:
    if(check[i]==0 and snt[i]==0):
        check[i]=1
        print(i,a.count(i))
