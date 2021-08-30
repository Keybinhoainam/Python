test=(int) (input())
for i in range(test):
    s=input()
    i=len(s)-2
    while(i>=0):
        if(s[i+1]<'5'):
            so=(int)(s[:(i+1)])
            tmp=(str)(so)
            s=tmp+(len(s)-i-1)*"0"
        else:
            so=(int)(s[:(i+1)])+1
            tmp=(str)(so)
            s=tmp+(len(s)-i-1)*"0"
        i-=1
    print(s)
    # if(len(s)>=2):
    #     if(s[1]<'5'):
    #         so=(int)(s[0])
    #         tmp=(str)(so)
    #         print(tmp+(len(s)-1)*"0")
    #     else:
    #         so=(int)(s[0])+1
    #         tmp=(str)(so)
    #         print(tmp+(len(s)-1)*"0")
    # else:
    #     print(s)


