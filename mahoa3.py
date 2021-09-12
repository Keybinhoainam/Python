def gt(s):
    return ord(s)-ord('A')
def r(s):
    tong=0
    for i in s:
        tong+=gt(i)
    tong=tong%26
    s=list(s)
    for i in range(len(s)):
        tong1=tong
        if(gt(s[i])+tong1>gt('Z')):
            tong1-=(gt('Z')-gt(s[i]))
            s[i]=chr(ord('A')+tong1-1)
        else:
            s[i]=chr(ord(s[i])+tong1)
    return s
def m(s1,s2):
    for i in range(len(s1)):

        tong1=ord(s2[i])-ord('A')
        if(gt(s1[i])+tong1>gt('Z')):
            tong1-=(gt('Z')-gt(s1[i]))
            s1[i]=chr(ord('A')+tong1-1)
        else:
            tmp=ord(s1[i])+tong1
            s1[i]=chr(tmp)
    print("".join(s1))

test=int(input())
for t in range(test):
    s=input()
    n=int(len(s)/2)
    s1=list(s[:n])
    s2=list(s[n:])
    s1=r(s1)
    s2=r(s2)
    m(s1,s2)

