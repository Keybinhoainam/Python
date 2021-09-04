test=int(input())
for t in range(test):
    n=input()
    check=0
    tong=int(ord(n[0]))-ord('0')
    for i in  range(1,len(n)):
        tong+=(ord(n[i])-ord('0'))
        if(abs(ord(n[i])-ord(n[i-1]))!=2):
            check=1
            break
    if(check==0 and tong%10==0):print("YES")
    else:print("NO")