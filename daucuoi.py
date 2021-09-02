test=int(input())
for i in range(test):
    s=input()
    a=int(s[:2])
    b=int(s[-2:])
    # print(a,b)
    if(a==b):print("YES")
    else: print("NO")