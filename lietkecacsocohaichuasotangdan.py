s=input()
n=len(s)
i=0
a=[]
while(i+1<n):
    a.append(int(s[i:i+2]))
    i+=2
a.sort()
# print(a)
b=set(a)
a=list(b)
a.sort()
# print(b)
for i in a:
    print(i,end=" ")
print()