import streamlit as st
import pandas as pd
import time
st.title('Lathiya Dhruvish')

st.header('i am learning data science')

st.subheader('Data science')

st.markdown("""
# Data Science
- numpy
- pandas
""")

st.code('''
def hello():
        return 02;
''')

st.latex('x^2')

df = pd.DataFrame({
    'name':['jay','raj'],
    'age':[1,3]
})

st.dataframe(df)

st.metric('Revenue','Rs','-10')

st.json({
    'name':['jay','raj'],
    'age':[1,3]
})

# st.image('https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg')

st.sidebar.title('dhruvish')

# col1 ,col2,col3 = st.columns(3)

# with col1: 
#     st.image('https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg')
# with col2:
#     st.image('https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg')
# with col3:
#     st.image('https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg')

st.error('login fails')
st.success('login success fully')

bar = st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

email = st.text_input('Enter of text')
password = st.text_input('Enter of password')

btn = st.button("Submit")

if btn:
    if email == 'dhruvish@gmail.com' and password == '1234':
        st.success('Login Successful') 
        st.balloons()
    else:
        st.error('Login failed')



# email = st.text_input('Enter of text')
# password = st.text_input('Enter of password')

# btn = st.button("Submit")

# if btn:
#     if email == 'dhruvish@gmail.com' and password == '1234':
#         st.success('Login Successful') 
#         st.balloons()
#     else:
#         st.error('Login failed')


file  = st.file_uploader('upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())

email = st.text_input('Enter of email = ')
nu = st.number_input('Enter of number ')
st.date_input("Enter register data ")

a = st.button('btn')
st.balloons()
ans = st.selectbox('Select gender ',['male','female'])
print(ans)