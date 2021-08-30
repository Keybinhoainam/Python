import math
def ktnt(a,b):
    if(b==0):return a
    else:return ktnt(b,a%b)
def snt(n):
    dem=0
    for i in range(1,n):
        if(n%i==0):dem+=1
    if(dem==1):return 1
    else: return 0
test=(int)(input())
for i in range(test):
    n=(int)(input())
    dem=0
    for i in range(n):
        if(ktnt(n,i)==1):
            dem+=1
            # print(i)
    # print(dem)
    if(snt(dem)==1): print("YES")
    else: print("NO")