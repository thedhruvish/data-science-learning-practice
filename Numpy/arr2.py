import numpy as np
arr = np.array([
    [
        [
            [11,12,13],
            [14,15,16]
        ],
        [
            [1,2,3],
            [4,5,6] # 5 6
        ]
    ],
    [
        [
            [1111,1112,1113],#1112 1115
            [1114,1115,1116]
        ],
        [
            [111,112,113], 
            [114,115,116]
        ]
    ]
])

# print(arr[1,0,0,0:2])
# a = np.array([],dtype='int')

# for i in range(0,10):
#     a = np.append(a,i)

# print(a)


print(arr.shape)