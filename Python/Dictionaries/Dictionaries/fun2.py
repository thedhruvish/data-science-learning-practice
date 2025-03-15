thisDic = {
    "name":"Om",
    "age":19,
    "city":"surat"
}

x = ("name","age","city")
y = 0

#thisdic = dict.fromkeys(x,y)
#print(thisdic)

#print(type(dict))


x = thisDic.setdefault("city","surat")

print(x)

print(thisDic)
