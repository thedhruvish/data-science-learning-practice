import numpy as np

# a = np.array([[1,2],[3,4]])

# print(a.T)

# np.save('test',a)

b = np.load('test.npy')

print(b)

# random 
from numpy import random as rd

# print(rd.randint(10))
# print(rd.randint(5))

# print(rd.randint(6,size=(2,3)))

# print(rd.choice([1,23,4,23,43,5]))

# print(np.around([1.1,1.32,1.65,4.3]))

print(np.floor([-1.1,1.32,1.65,4.3]))
print(np.ceil([-1.1,1.32,1.65,4.3]))