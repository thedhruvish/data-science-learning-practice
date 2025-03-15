import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11])

# print(np.where(a == 4)) # return index
print(a[a%2 == 0]) 
# print(np.where(a%2 == 0)) 

# print(np.searchsorted(a,5,side='right'))

a = np.array([1,2,3,6,7,8,9,10,11])

# print(np.searchsorted(a,[2,5]))

# arr = np.array([6, 7, 8])

# x = np.searchsorted(arr, 7,side='right' )
# print(x)
