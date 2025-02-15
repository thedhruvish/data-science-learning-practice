a = int(input("Enter of a : "))
b = int(input("Enter of b : "))
c = int(input("Enter of c : "))
d = int(input("Enter of d : "))
e = int(input("Enter of e : "))


if a < b and a < c and a < d and a < e:
    print("A is min")
elif b < c and b < d and b < e:
    print("B is min")
elif c < d and c < e:
    print("C is min")
elif d < e:
    print("D is min")
else:
    print("E is min")

