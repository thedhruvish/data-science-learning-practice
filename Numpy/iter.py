import numpy as np

a = np.array([1,2,3])

for i in a:
    print(i)

a = np.array([[1,2,3],[4,5,6]])

for i in a:
    for j in i:
        print(j)

a = np.array([[[1],[2],[3]],[[4],[5],[6]]])

for i in a:
    for j in i:
        for k in j:
            print(k)