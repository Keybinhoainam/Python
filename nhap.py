a=[1,'a','5','b']
b=[]
count=0
for i in a:
    if(i not in b):
        b.append(i)
        count+=1
print(count)