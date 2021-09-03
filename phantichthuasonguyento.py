import math
tmp1=1000_000
tmp=int(math.sqrt(tmp1))
check=[0]*(tmp1+5)
check[0]=check[1]=1
snt=[]
for i in range(2,tmp+1):
    if(check[i]==0):
        snt.append(i)
        j=i*i
        while(j<=tmp1):
            check[j]=1
            j+=i
for i in range(tmp+1,1000_000):
    # print(i,check[i])
    if(check[i]==0): snt.append(i)
# print(snt)
test=int(input())
for t in range(test):
    n=int(input())
    kq=[]
    i=0
    while(i<len(snt) and snt[i]<=n):
        n1=n
        while(n1%snt[i]==0):
            kq.append(snt[i])
            n1/=snt[i]
        i+=1
    res=[]
    res.append("1")
    i=0
    # check=[0]*n
    while(i<len(kq)):
        tmp2=str(kq[i])+"^"+str(kq.count(kq[i]))
        res.append(tmp2)
        i+=kq.count(kq[i])
    s=" * ".join(res)
    print(s)
