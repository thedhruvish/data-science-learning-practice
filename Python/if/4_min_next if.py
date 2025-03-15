a = int(input("Enter of a : "))
b = int(input("Enter of b : "))
c = int(input("Enter of c : "))
d = int(input("Enter of d : "))


if a < b :
    if a < c:
        if a < d:
            print("A is min")
        else:
            print("D is min")
    else:
        if c < d:
            print("C is min")
        else:
            print("D is min")   
else:
    if b < c:
        if b < d:
            print("B is min")
        else:
            print("D is min")
    else:
        if c < d:
            print("C is min")
        else:
            print("D is min")

