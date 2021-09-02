test=int(input())
for t in range(test):
    s=input()
    i=0
    s1=""
    while(i<len(s)):
        j=i+1
        while(j<len(s)and s[j]==s[i]):j+=1
        # print(s1,j-i,s[i])
        s1=s1+str(j-i)+s[i]
        i=j
        # print(s)
    print(s1)
