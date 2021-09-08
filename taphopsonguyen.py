def xuat(a):
    a.sort()
    for i in a:
        print(i,end=" ")
    print()
n,m=map(int,input().split())
a,b = set([int(i) for i in input().split()]), set([int(i) for i in input().split()])
a1,a2,a3=[int(x) for x in a.intersection(b)],[int(x) for x in a.difference(b)],[int(x) for x in b.difference(a)]
xuat(a1);xuat(a2);xuat(a3)
