def findFirstMissing(a,n):
    for i in range(n-1):
        if abs(a[i]-a[i+1])!=1:
            return i
    return n-1

n = int(input())
a = [int(i) for i in input().split()]
a.sort()
idx = findFirstMissing(a,n)
print(a[idx]+1)