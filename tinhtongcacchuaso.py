test=int(input())
for t in range(test):
    s=input()
    check=[]
    dem=0
    a=[]
    for i in s:
        if(ord(i)<=ord('Z') and ord(i)>=ord('A')):
            a.append(i)
        else:
            dem+=ord(i)-ord('0')
    a.sort()
    print(''.join(a),dem,sep="")
