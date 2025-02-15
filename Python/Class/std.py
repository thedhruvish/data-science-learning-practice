class Student:
    def __init__(self):
        self.rNo = int(input("Enter of Roll No:"))
        self.name = input("Enter of Name :")
        self.c = int(input("Enter of Mark in C :"))
        self.cpp = int(input("Enter of Mark in Cpp :"))
        self.python = int(input("Enter of Mark in Python :"))
        self.total = self.c + self.cpp + self.python
        self.avg = round(self.total / 3,2)
        self.min = min(self.c,self.cpp,self.python)
        self.max = max(self.c,self.cpp,self.python)
    def show(self):
        print(self.rNo,"\t",self.name,"\t",self.c,"\t",self.cpp,"\t",self.python,"\t",self.total,"\t",self.avg,"\t",self.min,"\t",self.max)

objArr = []

n = int(input("Enter of Total Student : "))

for i in range(n):
    print(f"Student Number {i+1} \n")
    obj = Student()
    objArr.append(obj)
    
print("RNO\tName\tc\tcpp\tpython\tTotal\tavg\tmin\tmax")
for i in objArr:
    i.show()
