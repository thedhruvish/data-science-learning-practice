a = int(input("Enter of a : "))
b = int(input("Enter of b : "))
c = int(input("Enter of c : "))
d = int(input("Enter of d : "))


if a < b and a < c and a < d:
    print("A is min")
elif b < c and b < d :
    print("B is min")
elif c < d:
    print("C is min")
else:
    print("D is min")

