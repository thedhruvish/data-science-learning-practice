x = lambda a,b: a + b

print(x(10,15))

def myfuct():
    return lambda a,b: a + b

f = myfuct()

print(f(10,20))

