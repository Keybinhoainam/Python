def kt(snt):
    n=500000
    check=[0]*(n+5)
    for i in range(2,n+1):
        if(check[i]==0):
            snt.append(i)
            j=i*i
            while(j<=n):
                check[j]=1

                j+=i
snt=[]
kt(snt)
n=int(input())
a=[int(x) for x in input().split()]
check=[0]*1005
b=[]
tong=0
for i in a:
    if(check[i]==0):
        check[i]=1
        b.append(i)
        tong+=i
# print(b)
vti=-1
tongl=0
for i in range(len(b)):
    tongl+=b[i]
    # print(tongl,tong-tongl)
    if(tongl in snt and (tong-tongl) in snt):
        vti=i
        break
# print(i)
if(vti==-1):print("NOT FOUND")
else: print(i)