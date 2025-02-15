import pandas as pd
import numpy as np

dt = np.array([1,2,3,4])
a = pd.Series(dt)
# b = pd.Series(dt,index=['a','b','c','d'])
# print(a)
# print(b)

# print(a[0])
# print(b['a'])


# print(pd.Series())

# dict
di = {'one':1,'two':2,'three':3,'four':4}

# print(pd.Series(di))

# print(pd.Series(2,index=[0,1,2,3,4]))

print(a)
print(a.index)
print(a.shape)
print(a.dtype)
print(a.empty)
print(pd.Series([1,2,np.nan]).hasnans)
print(pd.Series([1]).nbytes)

print(a.ndim)