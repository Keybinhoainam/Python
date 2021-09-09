def kt(s):
    n=len(s)
    for i in range(n):
        if(s[i]!=s[n-1-i]):return 0
    return 1

n,m=map(int,input().split())
a=[]
for i in range(n):
    b=[int(x) for x in input().split()]
    a.append(b)

maxnt=-1
for i in range(n):
    for j in range(m):
        tmp=str(a[i][j])
        if(kt(tmp)==1 and a[i][j]>maxnt and len(tmp)>=2):
            maxnt=a[i][j]
if(maxnt==-1):print("NOT FOUND")
else:
    print(maxnt)
    for i in range(n):
        for j in range(m):
            if(a[i][j]==maxnt):
                print(f"Vi tri [{i}][{j}]")