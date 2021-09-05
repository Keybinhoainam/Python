def kt1(s):
    vt=0
    check=1
    for i in s:
        if(vt%2==0 and ord(i)%2!=0):
            check=0
            break
        if(vt%2!=0 and ord(i)%2==0):
            check=0
            break
        vt+=1
    return check

def kt2(s):
    tong=0
    for i in s:
        tong+=ord(i)-ord('0')
    check=1
    if(tong<2):check=0
    for i in range(2,tong):
        if(tong%i==0):
            check=0
            break
    return check

test=int(input())
for i in range(test):
    s=input()
    # print(kt1(s),kt2(s),sep="\n")
    if(kt1(s) and kt2(s)):print("YES")
    else: print("NO")