test=int(input())
for t in range(test):
    s=input()
    s1=""
    i=0
    while(i<len(s)):
        s1=s1+s[i]*(int(s[i+1]))
        i+=2
    print(s1)