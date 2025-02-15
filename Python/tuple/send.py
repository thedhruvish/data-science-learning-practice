tup1 = (12,4,6,78,"hello",34,34.5)

print(tup1[0])
print(tup1[0:3])

if "hello" in tup1:
    print("Ok")


x = list(tup1)

x[0] = True

y = tuple(x)

print(type(y),y)


