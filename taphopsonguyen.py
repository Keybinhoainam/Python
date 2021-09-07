n,m=map(int,input().split())
a=[];b=[]
while(len(a)<n):
    s=input()
    for i in s.split():
        a.append(int(i))
while(len(b)<m):
    s=input()
    for i in s.split():
        b.append(int(i))
a.sort();b.sort()
a1=set(a);b1=set(b)
c1=list(a1.intersection(b1))
c1.sort()

for i in c1:
    print(i,end=" ")
print()
c2=[int(i) for i in a1 if(i not in b1)]
for i in c2:
    print(i,end=" ")
print()
c3=[int(i) for i in b1 if(i not in a1)]
for i in c3:
    print(i,end=" ")
print()
