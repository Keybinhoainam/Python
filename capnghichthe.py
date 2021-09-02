n=int(input())
a=[int(j) for j in input().split()]
dem=0
for i in range(n):
    for j in range(i+1,n):
        if(a[j]<a[i]):dem+=1
print(dem)