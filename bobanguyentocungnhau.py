def tao(hnt):
    n=200
    check=[0]*205
    for i in range(2,n+1):
        if(check[i]==0):
            hnt[i].append(i)
            j=i+i
            while(j<=n):
                check[j]=1
                hnt[j].append(i)
                j+=i
def kt(hnt,i,j,k):
    for i1 in hnt[i]:
        if(i1 in hnt[j] or i1 in hnt[k]):return 0
    for j1 in hnt[j]:
        if(j1 in hnt[k]):return 0
    return 1
l,r=map(int,input().split())
hnt=[[]*205]*205
for i in range(200):
    hnt[i]=[]
tao(hnt)
check=1
i=l
while(i<=r):
    j=i+1
    while(j<=r):
        k=j+1
        while(k<=r ):
            if(kt(hnt,i,j,k)==1):
                print(f"({i}, {j}, {k})")
            k+=1
        j+=1
    i+=1