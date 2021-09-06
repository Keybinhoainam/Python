import math
def kt(vtnt):
    n=10000
    check=[0]*(n+5)
    for i in range(2,n+1):
        if(check[i]==0):
            vtnt.append(i)
            j=i*i
            while(j<=n):
                check[j]=1
                j+=i
test=int(input())
for t in range(test):
    s=input()
    vtnt=[]
    snt=['2','3','5','7']
    kt(vtnt)
    n=len(s)
    dem=0
    for i in s:
        if(i in snt):dem+=1
    if(n in vtnt and dem>(n-dem)):print("YES")
    else:print("NO")