list1 = []

for i in range(0,5):
    a = int(input("Enter of Value : "))
    list1.append(a)

maxValue = list1[0]

for i in list1:
    if maxValue < i:
        maxValue = i

minValue = list1[0]

for i in list1:
    if minValue > i:
        minValue = i


print(maxValue)
print(minValue)

