a = int(input("Enter of a : "))
b = int(input("Enter of b : "))
c = int(input("Enter of c : "))
d = int(input("Enter of d : "))
e = int(input("Enter of e : "))


if a > b :
    if a > c:
        if a > d:
            if a > e:
                print("A is max")
            else:
                print("E is max")
        else:
            if d > e:
                print("D is max")
            else:
                print("E is max")
    else:
        if c > d:
            if c > e:
                print("C is max")
            else:
                print("E is max")
        else:
            if d > e:
                print("D is max")
            else:
                print("E is max")
else:
    if b > c:
        if b > d:
            if b > e:
               print("B is max")
            else:
               print("E is max") 
        else:
            if d > e:
                print("D is max")
            else:
                print("E is max")
    else:
        if c > d:
            if c > e:
                print("C is max")
            else:
                print("E is min")
        else:
            if d > e:
                print("D is max")
            else:
                print("E is max")
















            

