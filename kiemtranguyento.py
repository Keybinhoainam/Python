
import math
n,m=map(int,input().split())
a=[m*[]]*n
snt=[0]*1005
snt[1]=1
snt[0]=1
tmp=int(math.sqrt(1000))
for i in range(2,tmp+1):
    if(snt[i]==0):
        j=i*i
        while(j<=1000):
            snt[j]=1
            j+=i
for i in range(n):
    txt=input()
    a[i]=[int(x) for x in txt.split()]
for i in range(n):
    s=""
    for j in range(m):
        s=s+str(1-snt[a[i][j]])+" "
    print(s)
