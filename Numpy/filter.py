import numpy as np

arr = np.array([1,2,3,4])

x = [True,False,True,True]

# print(arr[x])


l = []

for i in arr:
    if i % 2 == 0:
        l.append(True)
    else:
        l.append(False)
print(arr[l])

arr = np.array([11,12,13,14,15,16])

l = arr > 13

print(l)

print(arr[l])