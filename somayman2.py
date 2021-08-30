test=(int)(input())
for i in range(test):
    s=input()
    dem=0
    for i in s :
        if(i=='4'or i=='7'):
            continue
        else: 
            dem=1
            break
    if(dem==0):print("YES")
    else: print("NO")