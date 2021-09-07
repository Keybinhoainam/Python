a=[]
for i in range(10):
    a.append(str(i))
for i in range(ord('A'),ord('Z')+1):
    a.append(chr(i))
test=int(input())
for t in range(test):
    n,b=map(int,input().split())
    kq=""
    while(n!=0):
        tmp=n%b
        kq=a[tmp]+kq
        n=int(n/b)
    print(kq)