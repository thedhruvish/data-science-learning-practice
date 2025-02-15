a = int(input("Enter of a : "))
b = int(input("Enter of b : "))
c = int(input("Enter of c : "))
d = int(input("Enter of d : "))


if a > b :
    if a > c:
        if a > d:
            print("A is max")
        else:
            print("D is max")
    else:
        if c > d:
            print("C is max")
        else:
            print("D is max")   
else:
    if b > c:
        if b < d:
            print("B is max")
        else:
            print("D is max")
    else:
        if c < d:
            print("C is max")
        else:
            print("D is max")

