# local 
# def demo():
#     a = 10
#     print(a)
# demo()


# def demo():
#     a = 15
#     def demo1():
#         print(a)
#     demo1()
# demo()


#gobal key word
# def demo():
#     global a 
#     a = 50
# demo()
# print(a)



def demo():
    a = 10
    def demo1():
        nonlocal a
        a = 20
    demo1()
    return a
print(demo())

