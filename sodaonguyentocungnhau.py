def uoc(n,n1):
    if(n1==0):return n
    return uoc(n1,n%n1)
test=int(input())
for t in range(test):
    n=(input())
    arr=list(n)
    arr.reverse()
    n1=''.join(arr)
    n=(int)(n)
    n1=int(n1)
    # print(n,n1,sep=" ")
    if(uoc(n,n1)==1):print("YES")
    else: print("NO")
