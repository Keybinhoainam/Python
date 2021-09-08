n,m=map(int,input().split())
a,b = set([int(i) for i in input().split()]), set([int(i) for i in input().split()])
if(a==b):print("YES")
else:print("NO")