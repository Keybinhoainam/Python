def mod(s,n):
    kq=0
    for i in s:
        kq=((kq * 10)+(ord(i)-ord('0')))%n
    return kq
test=int(input())
for i in range(test):
    s=input()
    if(mod(s,3)==0):print("YES")
    else: print("NO")