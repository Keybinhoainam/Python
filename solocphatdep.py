s=input()
check=1
for i in range(len(s)):
    if(s[i]=='6'):continue
    elif(s[i]=='8' and ((i-1>=0 and s[i-1]=='6')or (i-1>=0 and s[i-1]=='8' and s[i-2]=='6')) ):continue
    else:
        check=0
        break
if(check==1):print("YES")
else:print("NO")
        