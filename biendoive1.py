n=int(input())
while(n!=0):
    check=[0]*2000_000
    dem=1
    check[n]=1
    while(n!=1):
        if(n%2==0):n/=2
        else: n=(n*3)+1
        n=int(n)
        if(check[n]==0):
            dem+=1
            check[n]=1
    print(dem)
    n=int(input())