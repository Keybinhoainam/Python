n = int(input())
a=[int(x) for x in input().split()]
dem=0
for i in range(1,n):
    if(a[i]!=a[i-1]):dem+=1
print(dem)