import math
test=(int)(input())
for i in range(test):
    n,x,m=map(float,input().split())
    # print(n,x,m)
    # print(x+1)
    x/=100
    tmp=1+x
    kq=math.log(m/n,tmp)
    print(math.ceil(kq))
    