def uoc(n,n1):
    if(n1==0):return n
    return uoc(n1,n%n1)
test=1
for t in range(test):
    n,k=map(int,input().split())
    l=pow(10,k-1)
    r=pow(10,k)
    dem=0
    for i in range(l,r):
        if(uoc(i,n)==1):
            print(i,end=" ")
            dem+=1
        if(dem==10):
            print("\n")
            dem=0