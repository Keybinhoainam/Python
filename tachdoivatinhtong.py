s=input()
while(len(s)!=1):
    n=len(s)//2
    s1=s[:n];s2=s[n:]
    s=str(int(s1)+int(s2))
    print(s)