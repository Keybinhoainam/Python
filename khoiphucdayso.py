import numpy as np
import array as arr
n=(int)(input())
b=[[0]*n]*n
for i in range(n):
    txt=input()
    b[i]=[int(j) for j in txt.split()]
r=arr.array('i') #lưu giá trị tổng hàng
suma=0.0 #sum all
for i in range(n):
    sumrow=0
    for j in range(n):
        suma+=b[i][j]
        sumrow+=b[i][j]
    r.append(sumrow)
tong=suma/(2*n-2)
if(n==2):print(1,1)
else:
    a=arr.array('i')
    for i in range(n):
        tmp=(r[i]-tong)/(n-2)
        # print(r[i],"  ",tong)
        tmp=(int)(tmp)
        a.append(tmp)
    s=""
    for i in a:
        s=s+str(i)+" "
    print(s)