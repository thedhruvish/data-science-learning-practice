list1 = []
for i in range(0,5):
    a = int(input("Enter of Value : "))
    list1.append(a)

print("List Two:")

list2 = []
for i in range(0,5):
    a = int(input("Enter of Value : "))
    list2.append(a)

list3 = list1 + list2


print(list3)
