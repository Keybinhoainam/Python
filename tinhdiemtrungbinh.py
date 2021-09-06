n=int(input())
a=[float(x) for x in input().split()]
tong=0.000
for i in a:
    tong+=i
n1=max(a)
n2=min(a)
n3=a.count(n1)
n4=a.count(n2)
tong=tong-n1*n3-n2*n4
tong=tong/(len(a)-n3-n4)
print('%.2f'%tong)