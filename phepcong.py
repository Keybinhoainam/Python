s=input()
n=len(s)
i=0
a=[]
j=0
while(i<n):
    while(i<n and s[i]>='0' and s[i]<='9'): 
        i+=1
    so=(int)(s[j:i])
    a.append(so)
    while(i<n and (s[i]==' ' or s[i]=='+' or s[i]=='=') ): 
        i+=1
    j=i
if(a[0]+a[1]==a[2]):print("YES")
else: print("NO")
