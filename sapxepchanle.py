n=int(input())
a=[]
while(len(a)<n):
    s=input()
    for i in s.split():
        a.append(int(i))
chan=[]
le=[]
for i in range(n):
    if(a[i]%2==0):
        chan.append(a[i])
        a[i]=0
    else:
        le.append(a[i])
        a[i]=1
chan.sort();
le.sort(reverse=True);
ic=0;il=0
for i in range(n):
    if(a[i]==0):
        print(chan[ic],end=" ")
        ic+=1
    else:
        print(le[il],end=" ")
        il+=1




