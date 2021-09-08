n=int(input())
a=[int(x) for x in input().split()]
kq=n*max(a)
gt=a[0]
for i in a:
    tmp=0
    for j in a:
        tmp+=(abs(j-i))
    if(kq>tmp):
        kq=tmp
        gt=i
print(kq,gt)
