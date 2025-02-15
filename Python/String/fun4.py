t = "hello word "

print(t.rfind("d"))

print(t.rindex("d"))

print(t.rjust(50))

print(t.rpartition("w"))

print(t.rsplit(" "))

t = "     Hello           word        "

print(t.rstrip(),"google")

print(t.split("l"))

t = "hello \n wo\nrd"
print(t.splitlines())


print(t.startswith("hq"))

t = "     Hello           word        "

print(t.strip(),"ggg")

t = "Hello word "
print(t.swapcase())

print(t.title())

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

t = "hello word"
print(t.upper())


t = "40"
print(t.zfill(100))

