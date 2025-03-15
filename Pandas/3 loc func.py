import pandas as pd

ans={
    'design':pd.Series([1,2,3],index=['a','b','c']),
    'android':pd.Series([10,11,12],index=['a','b','c'])
}

df=pd.DataFrame(ans)

df['flutter']=pd.Series([20,30,40],index=['a','b','c'])
df['python']=df['design']+df['android']
print(df)
# print(df.loc['a'])
# print(df.loc[:'c'])
# print(df.loc[['a','c']])
# print(df.loc[:,['python']])
# print(df.loc[:,'android':'python'])
# print(df.loc[:,['android','python']])
# print(df.loc[::2,['python']])
# print(df.loc[:,'design'::2])

# print(df.loc[df['android'] == 11])

# iloc function

# print(df.iloc[1])
# print(df.iloc[::2])
# print(df.iloc[[0,2]])
# print(df.iloc[:,1])
# print(df.iloc[:,::2])
# print(df.iloc[:,[1,3]])

# df.drop(0)
# print(df)

a1=pd.DataFrame([[10,12],[21,22]],columns=['a','b'])
b1=pd.DataFrame([[33,44],[55,66]],columns=['a','b'])
print(a1)
print(b1)
c1=pd.concat([a1,b1])
print(c1)
d1=c1.drop(0)
print(d1)