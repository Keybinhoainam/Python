test=int(input())
f=[0]*100
f[1]= 1
f[2]=1
# f[2]=1
i=3
while(i<93):
    f[i]=f[i-1]+f[i-2]
    i+=1
for t in range(test):
    kq=[]
    a,b=map(int,input().split())
    i=1
    while(i<a):i+=1
    while(i>=a and i<=b):
        kq.append(str(f[i]))
        i+=1
    s=' '.join(kq)
    print(s)
    # print(kq)
