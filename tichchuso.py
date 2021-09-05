def tich(s):
    kq=1
    for i in s:
        if(i!='0'):
            kq*=int(ord(i)-ord('0'))
    return kq
test=int(input())
for i in range(test):
    s=input()
    print(tich(s))