def hello():
    print("hello")

#hello()

def hello1(a = 10,b = 20):
    print(a + b)
    
#hello1(20,5)
#hello1(b=10,a=10)

def helo2(n,*key):
    print(key,"new = ",n)

helo2(10,20,9)

def h1():
    def h2():
        print("hello miten")
        
    print("new")
    return h2

#x = h1()
#x()



