# int are not Working
a = ['45','4323','435','46','57','78','90','75',"75"]
b = []
"""
for i in a:
    if '4' in i:
        b.append(i)
"""
#print(b)

b = [x for x in a if x =="46"]

#print(b)

#a.sort()

#a.sort(reverse = True)

#b = a.copy()
#print(a+b)
b = list(a)

#print(a)
#demo = ["hello"]
#b.extend(demo)

print(a.count("75"))

print("\n\n\n b = ",b)




