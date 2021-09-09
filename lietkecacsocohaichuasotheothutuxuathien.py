
s=input()
n=len(s)
i=0
a=[]
b=[]
while(i+1<n):
    tmp=int(s[i:i+2])
    if(tmp not in a):b.append(tmp)
    a.append(tmp)
    i+=2
for i in b:
    print(i,end=" ")
    # print(i,end=" ")