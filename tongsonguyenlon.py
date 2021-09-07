def gt(s):
    return ord(s)-ord('0')

a=input()
b=input()
while(len(a)<len(b)):
    a='0'+a
while(len(b)<len(a)):
    b='0'+b
i=len(a)-1
nho=0
kq=""
while(i>=0):
    tong=(gt(a[i])+gt(b[i]))+nho
    nho=int(tong/10)
    kq=str(tong%10)+kq

    i-=1
if(nho>0):kq=str(nho)+kq
i=0
while(i<len(kq)-1 and kq[i]=='0'):i+=1
kq=kq[i:]
print(kq)