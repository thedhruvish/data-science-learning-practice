# import time
# import numpy as np

# start_list = time.time()
# li = list(range(0,10000))

# for i in li:
#     i = i ** 1000

# end_list = time.time()

# print(end_list-start_list)


# start_list = time.time()
# np_array = np.arange(0,10000)
# np_array = np_array ** 1000
# end_list = time.time()
# print(end_list-start_list)

# import numpy as np
import numpy  as np

# print(np.randint(0,100))

# print(np.linspace(0,9,4))


# 0 1 2 3 4 5 6 7 8 9 10

# print(np.zeros((3,2)))


# for i in np.arange(0.2,10):
#     print(i)

# for i in range(0,10):
#     print(i)
a = np.array([1,True,'ok',2.2,4j,None])

for i in a:
    print(type(i))
print(a)

print(type(4j)) 