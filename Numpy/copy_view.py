import numpy as np

a = np.array([1,2,3,4])

#copy
# b = a.copy()

#views
b = a
b = a.copy()

a[0] = 10

print(a)
print(b)
