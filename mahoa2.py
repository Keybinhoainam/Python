p="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
s=[str(x) for x in input().split()]
while(s[0]!="0"):
    k=int(s[0])
    p1=""
    for i in range(len(s[1])):
        p1=p[(i+k)%28]+p1
        # print(p,s[1][(i+k)%len(s[1])],s[1])
    print(p1)
    s=[str(x) for x in input().split()]
