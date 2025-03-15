import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='StartUp Anaylsis')

df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')

investor_lists = df['investors'].fillna('').str.split(',')
all_investors = sum(investor_lists.tolist(), [])
all_investors = [investor.strip() for investor in all_investors]


def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 invertments of invetor
    last_5df = df[df['investors'].str.contains(investor,na=False)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Mos Recent Investments')
    st.dataframe(last_5df)
 
    #Biggest Investment
    col1 ,col2 = st.columns(2)
    st.subheader('Biggest Investments')
    with col1:
        big_inve = df[df['investors'].str.contains(investor,na=False)].groupby('startup')['amount'].sum().sort_values(ascending=True).head()
        # st.dataframe(big_inve)
        fig,ax = plt.subplots()
        ax.bar(big_inve.index,big_inve.values)
        st.pyplot(fig)
    
    with col2:
        verical_series = df[df['investors'].str.contains(investor,na=False)].groupby('vertical')['amount'].sum()
        fig1,ax1 = plt.subplots()
        ax1.pie(verical_series,labels=verical_series.index,autopct='%0.01f%%')
        st.pyplot(fig1)

    col3 ,col4 = st.columns(2)
    with col3:
        round_series = df[df['investors'].str.contains(investor,na=False)].groupby('round')['amount'].sum()
        fig2,ax2 = plt.subplots()
        ax2.pie(round_series,labels=round_series.index,autopct='%0.01f%%')
        st.pyplot(fig2)
    with col4:
        city_series = df[df['investors'].str.contains(investor,na=False)].groupby('city')['amount'].sum()
        print(city_series)
        fig3,ax3 = plt.subplots()
        ax3.pie(city_series,labels=city_series.index,autopct='%0.01f%%')
        st.pyplot(fig3)

    print(df.info())
    df['year'] = df['date'].dt.year
    df['year'] = df['year'].fillna(-1)      
    df['year'] = df['year'].astype('int')
    year_series = df[df['investors'].str.contains(investor,na=False)].groupby('year')['amount'].sum()
    print(year_series)
    fig4,ax4 = plt.subplots()
    ax4.plot(year_series.index,year_series.values)
    st.pyplot(fig4)  


st.sidebar.title('Startup Funding Anaysis')


option = st.sidebar.selectbox('Select one',['Ownerall Analysis','StartUp','Investor'])

if option == 'Ownerall Analysis':
    st.title('Overall Analysis')
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique()))
    st.title('StartUp Analysis')
    btn1 = st.sidebar.button('StartUp Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select StartUp',set(all_investors))
    btn2 = st.sidebar.button('Investors Analysis')
    if btn2:
        load_investor_details(selected_investor)
