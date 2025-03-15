list1 = []
for i in range(0,5):
    a = int(input("Enter of Value : "))
    list1.append(a)

list2 = []

for i in list1:
    list2.insert(0,i)

print(list2)
