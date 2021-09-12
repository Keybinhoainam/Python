import math
test=int(input())
for i in range(test):
    n=int(input())
    n1=2*n
    tmp=int(math.sqrt(n1))
    dem=0
    #x la so chu so nguyen duong lien tiep 
    for x in range(2,tmp+1):#vi sonho=(2*n/x -x +1)/2 nen de sonho khong am chay tu 2 den sqrt(2*n)
        tmp2=int(n1/x)-x+1
        sonho=int(tmp2/2)
        solon=sonho+x-1
        if(n1%x==0 and tmp2%2==0 and sonho>=1 and solon>sonho):dem+=1
    print(dem)