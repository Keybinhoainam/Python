import math
def kt(vtnt):
    n=500
    check=[0]*505
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
    snt=[2,3,5,7]
    vtnt=[]
    kt(vtnt)
    vt=0
    check=1
    for i in s:
        tmp=ord(i)-ord('0')
        if(vt in vtnt   and   tmp not in snt):
            check=0
            break
        if(vt not in vtnt   and   tmp in snt):
            check=0
            break
        vt+=1
    if(check==1):print("YES")
    else: print("NO")