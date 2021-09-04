n=int(input())
a=[int(x) for x in input().split()]
a.sort()
i=0
while(i<n-1):
    if((a[i+1]-a[i])!=1):
        break
    i+=1
# index=i
print(a[i]+1)