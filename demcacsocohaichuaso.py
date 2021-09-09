
s=input()
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
for i in b:
    print(i,c[i])
    # print(i,end=" ")