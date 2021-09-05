test=int(input())
for t in range(test):
    s=input()
    tong=0
    tich=1
    check=0
    vt=0
    for i in s:
        if(vt%2==0):
            tong+=ord(i)-ord('0')
        else:
            if(i!='0'):
                check=1
                tich*=(ord(i)-ord('0'))
        vt+=1
    if(check==0):tich=0
    print(tong,tich,sep=" ")