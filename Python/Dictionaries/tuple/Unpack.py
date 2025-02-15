tup1 = ("Raj","Ram","Ronak","Rahul")
tup2 = (1,3,5,7,7,8)

(a,b,*c) = tup1

print(a,b,c)

print(type(c))

for i in range(len(tup1)):
    print(tup1[i])

tup3 = tup1 *2  + tup2 

print(tup3)


print(tup1.count(1))

print(tup1.index("Raj"))
