def tongcs(n):
    tong=0
    while(n>0):
        tong=tong + n%10
        n=n//10
    return tong

def kq(a,n):
    res=[]
    for i in range(n):
        res.append([tongcs(a[i]),a[i]])
    res.sort()
    for i in range(n):
        print(res[i][1],end=" ")
    print("")

test=int(input())
for t in range(test):
    n=int(input())
    a=[int(x) for x in input().split()]
    kq(a,n)

# 1                                                          huso.py", line 12, in kq
# 8
# 143 43 22 99 7 9 1111 10000000