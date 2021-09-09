n,m=map(int, input().split())
a=[int(x) for x in input().split()]
b=[0]*(m+5)
a1=[]
for i in range(1,m+1):
    a1.append(i)
    b[i]=a.count(i)
for i in range(m):
    for j in range(m-1):
        if(b[a1[j]]<b[a1[j+1]]):
            a1[j],a1[j+1]=a1[j+1],a1[j]
        elif(b[a1[j]]==b[a1[j+1]] and a1[j]>a1[j+1]):
            a1[j],a1[j+1]=a1[j+1],a1[j]

max1=b[a1[0]]
i=0
while(i<m and (b[a1[i]]==max1 or b[a1[i]]==0)):i+=1
if(i==m):print("NONE")
else: print(a1[i])


