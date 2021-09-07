test=int(input())
for t in range(test):
    n,m,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input().split()]
    a.sort();b.sort();c.sort();
    check=0
    i=j=z=0
    while(i<n and j <m and z<k):
        if(a[i]==b[j] and b[j]==c[z]):
            print(a[i],end=" ")
            i+=1;j+=1;z+=1
            check=1
            
        elif(a[i]<b[j]):i+=1
        elif(b[j]<c[z]):j+=1
        else: z+=1
        # print(i,j,k)
    if(check==0):print("NO")
    print('')


