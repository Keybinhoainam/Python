test=10
dem=0
check=[0]*43
while(test>0):
    s=input()
    a=[int(x) for x in s.split()]
    for i in a:
        tmp=i%42
        if(check[tmp]==0):
            check[tmp]=1
            dem+=1
    test-=len(a)
print(dem)
