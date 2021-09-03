def check(a,b):
    if(b==0):return a
    return check(b,a%b)
n=int(input())
a=[int(x) for x in input().split()]
a.sort()
for i in range(n):
    for j in range(i+1,n):
        if(check(a[i],a[j])==1):
            print(a[i],a[j])


