test=int(input())
for t in range(test):
    s=input()
    n=input()
    i=0
    s1=len(s)
    n1=len(n)
    dem=0
    while(i<len(s)):
        while(i<s1 and s[i]!=n[0]):i+=1
        if(i+n1-1<s1 and s[i:i+n1]==n):
            dem+=1
            i+=n1
        else: i+=1
    print(dem)