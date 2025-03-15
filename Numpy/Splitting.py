import numpy as np

a = np.array([1,2,3,4,5])

newarr = np.array_split(a,3)
# newarr = np.array_split(a,4)

# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

#2 D array

a = np.array([[1,2,3],[4,5,6],[7,8,9],[11,12,13]])

newarr = np.array_split(a,3,axis=1)

print(newarr)