test=int(input())
for t in range(test):
    n=int(input())
    if(n%2==0):i=2
    else: i=1
    tong=0.00
    while(i<=n):
        tong+=(1/i)
        i+=2
    print('%.6f'%tong)