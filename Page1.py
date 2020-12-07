import streamlit as st
import pandas as pd
import requests
from io import StringIO

def app():
    st.title('AirBnB in Berlin')
    st.write('Top 10 Neighbourhoods with the more AirBnB Entire flat listings')


    DATA_URL = 'https://ndownloader.figshare.com/files/25533041'

    @st.cache(persist=True)
    def load_data():
        url = requests.get(DATA_URL)
        csv_raw = StringIO(url.text)
        data = pd.read_csv(csv_raw, low_memory=False,index_col=0)
        #data['date'] = pd.to_datetime(data['date'])
        return data

    df = load_data()

    top10 = df.loc[df.date == '2020-05-14']['neighbourhood_cleansed'].value_counts()[:10].index.tolist()
    df2=df.groupby(['neighbourhood_cleansed','date'],as_index=False).count()[['neighbourhood_cleansed','date','id']]
    df2.date = pd.to_datetime(df2.date, format='%Y-%m-%d')



    import plotly.express as px

    toplot = df2.loc[df2['neighbourhood_cleansed'].isin(top10)]
    fig = px.line(toplot, x="date", y="id", color='neighbourhood_cleansed')

    st.plotly_chart(fig)

