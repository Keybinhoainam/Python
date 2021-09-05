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
    kt(vtnt)
    if(int(s[-4:]) in vtnt):print("YES")
    else:print("NO")