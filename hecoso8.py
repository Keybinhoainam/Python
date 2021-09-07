s=input()

kq=""
# print(len(s))
while(len(s)%3!=0):
    s="0"+s
i=len(s)-1
# print(s)
while(i>=0):
    j=i
    index=0
    tmp1=0
    while(j>i-3):
        tmp=(ord(s[j])-ord('0'))
        tmp1+=tmp*pow(2,index)
        index+=1
        j-=1
    kq=str(tmp1)+kq
    i-=3
print(kq)
