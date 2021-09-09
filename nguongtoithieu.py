
s=input()
k=int(input())
n=len(s)
i=0
a=[]
b=[]
c=[0]*100
while(i+1<n):
    tmp=int(s[i:i+2])
    if(tmp not in a):b.append(tmp)
    a.append(tmp)
    c[tmp]+=1
    i+=2
b.sort()
check=0
for i in b:
    if(c[i]>=k):
        print(i,c[i])
        check=1
    # print(i,end=" ")
if(check==0):print("NOT FOUND")