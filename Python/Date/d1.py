import datetime

x = datetime.datetime.now()

print(x.year)

print(x.strftime("%d"))
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%M"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%h"))
print(x.strftime("%I"))
print(x.strftime("%p"))


x = datetime.datetime(2024, 7, 10)

print(x)

print(type(datetime.datetime.now))
