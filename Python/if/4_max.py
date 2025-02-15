a = int(input("Enter of a : "))
b = int(input("Enter of b : "))
c = int(input("Enter of c : "))
d = int(input("Enter of d : "))


if a > b and a > c and a > d:
    print("A is max")
elif b > c and b > d:
    print("B is max")
elif c > d:
    print("C is max")
else:
    print("D is max")

