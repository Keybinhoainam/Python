n,m=map(int,input().split())
a=[]
for i in range(n):
    b=[int(x) for x in input().split()]
    a.append(b)

max1=-1
min1=10005
for i in range(n):
    for j in range(m):
        if(max1<a[i][j]):
            max1=a[i][j]
        if(min1>a[i][j]):
            min1=a[i][j]
check=0
luck=max1-min1
for i in range(n):
    for j in range(m):
        if(a[i][j]==luck):
            check=1
            break
    if(check==1):break
if(check==0):print("NOT FOUND")
else:
    print(luck)
    for i in range(n):
        for j in range(m):
            if(a[i][j]==luck):print(f"Vi tri [{i}][{j}]")
            