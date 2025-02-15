list1 = []
for i in range(0,5):
    a = int(input("Enter of Value : "))
    list1.append(a)




idxNumber = int(input("Enter of Index Number : "))
Vale = int(input("Enter of Number to Be Insert on List : "))

for i in range(0,5):
    if i == idxNumber:
        list1[i] = Vale
    


print(list1)
