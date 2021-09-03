a,k,n=map(int,input().split())
if(a%k!=0):i=k-(a%k)
else: i=k
tmp=[]
while(i<=n-a):
    tmp.append(str(i))   
    i+=k
if(len(tmp)==0):print(-1)
else:
    tmp=list(tmp)
    s=' '.join(tmp) 
    print(s)
