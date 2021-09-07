test=int(input())
for i in range(1,test+1):
    s1=input()
    s2=input()
    a1=list(s1);a2=list(s2)
    a1.sort();a2.sort()
    print("Test "+str(i)+":",end=" ")
    if(a1==a2):print("YES")
    else:print("NO")