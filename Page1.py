import streamlit as st
import pandas as pd

def app(df,geojson_file,l_date,center):
    st.write('## Top Neighbourhoods with more flat listings on AirBnB')

    top15 = df.loc[df.date == l_date ]['neighbourhood_cleansed'].value_counts().loc[lambda x : x>200].index.tolist()
    top0 = df.loc[df.date == l_date ]['neighbourhood_cleansed'].value_counts().loc[lambda x : x>70].index.tolist()
    df2=df.groupby(['neighbourhood_cleansed','date'],as_index=False).count()[['neighbourhood_cleansed','date','id','price']]
    df2.date = pd.to_datetime(df2.date, format='%Y-%m-%d')



    import plotly.express as px

    toplot = df2.loc[df2['neighbourhood_cleansed'].isin(top15)]
    fig = px.line(toplot, x="date", y="id", color='neighbourhood_cleansed')
    fig.update_yaxes(title_text='number of listings')

    st.plotly_chart(fig)

    df3 = df.groupby(['neighbourhood_cleansed', 'date'], as_index=False).median()[
        ['neighbourhood_cleansed', 'date', 'id', 'price']]
    df3.date = pd.to_datetime(df2.date, format='%Y-%m-%d')
    topprice = df3.loc[df2['neighbourhood_cleansed'].isin(top15)]
    fig2 = px.line(topprice, x="date", y="price", color='neighbourhood_cleansed')
    fig2.update_yaxes(title_text='Median price per night')
    st.plotly_chart(fig2)

    import json

    with open(geojson_file,encoding ='utf-8') as json_file:
        data = json.load(json_file)

    import plotly.express as px

    dfmap = df.loc[df.date == l_date ]
    dfmap = dfmap.groupby(['neighbourhood_cleansed'], as_index=False).median()[
        ['neighbourhood_cleansed','id', 'price']]
    dfmap = dfmap.loc[dfmap['neighbourhood_cleansed'].isin(top0)]

    fig3 = px.choropleth_mapbox(dfmap, geojson=data, locations='neighbourhood_cleansed',
                               featureidkey="properties.neighbourhood", color='price',

                               mapbox_style="carto-positron",
                               zoom=10, center={"lat": center[0], "lon": center[1]},
                               opacity=0.5
                               )
    fig3.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig3)


