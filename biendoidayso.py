import math
def test(a):
    for i in range(1,len(a)):
        if(a[i]!=a[i-1]): return 0
    return 1


s=input()
while(s!="0 0 0 0"):
    a=[int(x) for x in s.split()]
    dem=0
    while(test(a)==0):
        b=[]
        for i in range(4):
            b.append(a[i])
        for i in range(3):
            # tmp=a[i]-a[i+1]
            b[i]=abs(a[i]-a[i+1])
        b[3]=abs(a[3]-a[0])
        a=b
        dem+=1
    print(dem)
    s=input()
