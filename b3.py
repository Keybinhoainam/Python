def power(x,y):
    if(x<0 or y<0):return 0
    if(x==0):return 0
    if(y==1):return x
    return x*pow(x,y-1)
print(power(2,3))