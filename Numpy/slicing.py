import numpy as np 

arr1 = np.array( 
   [ 
        [1,2,3],[4,5,6], 
        [7,8,9],[10,11,12] 
    ] 
)

# print(arr1[2:,1]) 
a = np.array([[[1,2,3,4],[5,6,7,8]]]) 
# print(type(a)) 
# print(a[0][0:2][1]) 

a = np.array([
    [[1,2,3]],
    [[4,5,6]],
    [[7,8,9]],
    [[10,11,12]],
])

print(a[1:,0:,1])