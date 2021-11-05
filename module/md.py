class Person:
    def __init__(self,ten,gioitinh,ngaysinh) :
        self.ten=ten
        self.gioitinh=gioitinh
        self.ngaysinh=ngaysinh
    def desc_Person(self) :
        print("thong tin:",self.ten,self.gioitinh,self.ngaysinh,end=" ")

class Student(Person):
    def __init__(self,ten,gioitinh,ngaysinh,msv,dtb,email) :
        super().__init__(ten,gioitinh,ngaysinh)
        self.msv=msv
        self.dtb=dtb
        self.email=email
    def desc_Student(self) :
        self.desc_Person()
        print(self.msv,self.dtb,self.email)
    def check_hoboc(self):
        if self.dtb>=3.2:
            print("co hoc bong")
        else: print("khong co hoc bong")

class Rectangle:
    def __init__(self,d,r):
        self.d=d
        self.r=r
    def chuvi(self):
        print((self.d+self.r)*2)

    def dientich(self):
        print((self.d*self.r))
        