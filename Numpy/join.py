import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

# print(arr)


# print(np.stack((arr1,arr2),axis=1))
# print(np.hstack((arr1,arr2)))
# print(np.vstack((arr1,arr2)))
print(np.dstack((arr1,arr2)))