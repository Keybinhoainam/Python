
def doics(n,b):
    kq=""
    while(n>0):
        tmp=n%b
        kq+=str(tmp)
        n//=b
    return kq==kq[::-1]
def ktcs2(c,a,b):
    for i in range(a,b+1):
        if(doics(i,2)):c.append(i)
    return c
a,b,m=map(int,input().split())
c=[]
c = ktcs2(c,a,b)
dem=0
i=0
for i in c:
    check=1
    if(doics(i,m)==False):
        i+=1
        continue
    for j in range(3,m):
           
        if(doics(i,j)==False):
            check=0
            break

    if(check==1):dem+=1
if(a==0):print(dem+1)
else: print(dem)