import math
def kt(n):
    mid=int(math.sqrt(n))
    check=0
    for i in range(2,mid+1):
        if(n%i==0):
            check=1
            break
    return check
test=int(input())
for i in range(test):
    s=input()
    tong=0
    for i in s:
        tong+=ord(i)-ord('0')
    if(kt(tong)==0):print("YES")
    else: print("NO")