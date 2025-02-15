thisdic = {"name":"Paleji","year":123}
"""

a = thisdic["name"]

#print(a)

b = thisdic.get("year")
#print(b)

c = thisdic.keys()
#print(c)


thisdic["year"] = 23
#print(thisdic)

d = thisdic.values()
#print(d)

e = thisdic.items()
#print(e)

if "name" in thisdic:
    print("Yes")
else:
    print("No")



thisdic.update({"year":999})

"""


thisdic["color"] = "Red"
thisdic.update({"Brith":"18 dec"})

#thisdic.pop("Brith")
thisdic.popitem()

#del thisdic
#thisdic.clear()

print(thisdic)
