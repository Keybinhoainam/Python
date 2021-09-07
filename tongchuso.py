s=input()
# print(s,len(s))
dem=0
if(s!='6'):
    while(len(s)>  1):
        # print("OK")
        tong=0
        for i in s:
            tong+=ord(i)-ord('0')
        # print(tong)
        s=str(tong)
        dem+=1
    print(dem)
else:print('1')