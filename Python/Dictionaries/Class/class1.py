
class frist:
    a = 50
    def hello(self,b):
        print("hello word",b)
        print(self.a)

#obj = frist()
#print(obj.a)
#obj.hello(20)


class second:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def h1(self):
        print("hello 2\n",self.a,self.b)

#obj = second(10,20)
#obj.h1()


class thried:
    a = 10
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self):
        print("helllo")
    def __str__(self):
        #return f"{self.name}({self.age})"
        def hello():
            print("hello")
        return
    
obj = thried("Om",18)
#obj.hello()
#print(obj)

#obj.a = 40
print(obj.a)

#del obj.a
#print(obj.a) Error



















