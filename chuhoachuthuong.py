s=input()
ct,ch=0,0

for i in s:
    if(i>='a' and i<='z'):ct+=1
    if(i>='A' and i<='Z'):ch+=1
if(ct>=ch): print(s.lower())
else: print(s.upper())