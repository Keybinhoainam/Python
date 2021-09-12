test=int(input())
for t in range(test):
    n,p=map(int,input().split())
    dem=0
    for i in range(2,n+1):
        j=i
        while(j%p==0):
            dem+=1
            j/=p
    print(dem)