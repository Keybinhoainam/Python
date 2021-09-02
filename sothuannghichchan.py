
def kt(a,l,s):
    if(len(s)==0):i=2
    else: i=0
    while(i<=8):
        s1=s
        s1=s1+str(i)
        if(len(s1)==l):
            s2=list(s1)
            s2.reverse()
            s2=''.join(s2)
            s1=s1+s2
            a.append(int(s1))
            # print(l,s1)
        else: kt(a,l,s1)
        i+=2


def kq(a):
    for i in range(1,4):
        kt(a,i,"")


a=[]
kq(a)
# a.sort()
test=int(input())
for t in range(test):
    n=int(input())
    i=0
    s=""
    while(i<len(a)):
        if(a[i]<n):
            s=s+str(a[i])+" "
            i+=1
        else: break
    print(s)