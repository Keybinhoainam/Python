s=input()
a=list(s)
i=len(a)-3
while(i>0):
    a.insert(i,',')
    i-=3
kq=''.join(a)
print(kq)