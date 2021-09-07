n=int(input())
while(n!=0):
    a=[]
    while(len(a)<n):
        tmp=input()
        i=0
        while(i<len(tmp)):
            if(tmp[i]!='0'):
                break
            i+=1
        tmp=tmp[i:]
        a.append(tmp)
    a.sort(reverse=True)
    a.sort(key=len,reverse=True)
    # print(a)
    if(a[0]!=a[-1]):print(a[-1],a[0],sep=" ")
    else: print("BANG NHAU")

    




    n=int(input())
        
