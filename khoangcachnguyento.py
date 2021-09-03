import math
n,x=map(int,input().split())
check=[0]*1000_005
check[0]=check[1]=1
snt=[]
for i in range(2,1001):
    if(check[i]==0):
        snt.append(i)
        j=i*i
        while(j<=1000_000):
            check[j]=1
            j+=i
for i in range(1000,1000_000):
    if(check[i]==0): snt.append(i)
s=str(x)+" "
tmp=x
for i in range(n):
    tmp=tmp+snt[i]
    s=s+str(tmp)+" "
print(s)
