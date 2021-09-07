n=int(input())
a=[[]*n]*n
tong=0
for i in range(n):
    s=input()
    a[i]=list(s)
    n1=a[i].count('C')
    tong+=int(n1*(n1-1)/2)
for i in range(n):
    n1=0
    for j in range(n):
        if(a[j][i]=='C'):n1+=1
    tong+=int(n1*(n1-1)/2)
print(tong)
