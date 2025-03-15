try:
    print(62/0)
except ArithmeticError:
     print("Arithmetic Error")

try:
    x = 1
    y = 0
    assert y != 0, "Invalid Operation" # denominator can't be 0
    print(x / y)
except AssertionError:
    print("AssertionError")

try:
    a = 10
    a.append(0)
    print(a)
except AttributeError:
    print("AttributeError")



n = int(input()) 
print(n * 10)


