import math
class CheckN:
    def __init__(self,a):
        self.a=a
    
    def party_check(self):
        if(self.a%2==0):return "chan";
        return "le"
    def is_prime(self):
        if(self.a<2):return "khong la so nguyen to"
        for i in range(2,self.a):
            if(self.a%i==0):return "khong la so nguyen to"
        return "la so nguyen to"
    def is_perfect(self):
        if(self.a<=1):return "khong la so hoan hao"
        tong=0
        for i in range(1,n):
            if(self.a%i==0):tong+=i
        if(tong==self.a):return "la so hoan hao"
        return "khong la so hoan hao"
    def is_square(self):
        tmp=math.sqrt(self.a)
        if (int)(tmp)==tmp:return "khong ..."
        return "co ..."

    
