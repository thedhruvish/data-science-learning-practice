import pandas as pd

# a = pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10]})
# print(a)

data = {
    'a':['jay','om','raj'],
    'b':[2,3,3],
    'c':[1,3,2]
}

# print(pd.DataFrame(data,index=[0,9,8]))

df = pd.DataFrame(data)
print(df.loc[[0,1]])
