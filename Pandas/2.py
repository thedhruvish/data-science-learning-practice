import pandas as pd

# df = pd.DataFrame()
# print(df)

# df = pd.DataFrame([1,2,3,4,5])
# print(df)

# di = {'No':[1,2,3],'name':['jay','raj','ram']}
# df = pd.DataFrame(di)
# print(df)

ans={
    'design':pd.Series([1,2,3],index=['a','b','c']),
    'android':pd.Series([10,11,12],index=['a','b','c'])
}
df = pd.DataFrame(ans)
# print(df)
# print(df['design'])

df['flutter'] = pd.Series([20,30,40],index=['a','b','c'])
# print(df)


df['python'] = df['flutter'] + df['design']

del df['design']

df.pop('flutter')

# print(df)
print(df.loc['a'])
