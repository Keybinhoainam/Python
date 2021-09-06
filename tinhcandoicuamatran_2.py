n=int(input())
a=[]
for i in range(n):
    b=[int(x) for x in input().split()]
    a.append(b)
k=int(input())
tongc=0
tongp=0
for i in range(n):
    for j in range(n):
        if(i+j<n-1):tongc+=a[i][j]
        if(i+j>n-1):tongp+=a[i][j]
dcl=abs(tongc-tongp)
if(dcl<=k):print("YES")
else: print("NO")
print(dcl)