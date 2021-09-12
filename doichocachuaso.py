
test=int(input())
for t in range(test):
    s=input()
    s1=len(s)
    s=list(s)
    index=-1
    for i in range(s1-2,-1,-1):
        if(int(s[i])>int(s[i+1])):
            index=i
            break
    vt=index+1
    for j in range(s1-1,index,-1):
        if(int(s[j])<int(s[index]) and int(s[j])>=int(s[vt])):
            vt=j
    if(index==-1 or (index==0 and s[vt]=='0')):print(-1)
    else:
        s[index],s[vt]=s[vt],s[index]
        print(''.join(s))



    
    