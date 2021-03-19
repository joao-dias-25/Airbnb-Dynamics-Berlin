import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

import datetime

def app(df,geojson_file, l_date,center):
    col1, col2 = st.beta_columns(2)

    with col1:
        st.write('## Entire Flat AirBnB listings density')

    df=df[['latitude', 'longitude', 'date']]
    #df.date = pd.to_datetime(df.date, format='%Y-%m-%d')
    with col2:
        y=st.selectbox('date', df.date.unique(), index=(len(df.date.unique())-1))
    df2=df.loc[df.date==y]


    import plotly.express as px
    import plotly.figure_factory as ff

    # it needs a token for access mapbox
    px.set_mapbox_access_token(
        'pk.eyJ1Ijoiam9obnppbnoiLCJhIjoiY2tmbWthazZ6MDNueDJxb2ZyZ2M3czU0dyJ9.Bl3T4kl14xan7glGxid_Rw'
                                    )

    lat = df2['latitude']
    lon = df2['longitude']
    frame = df2['date']

    fig = ff.create_hexbin_mapbox(
        lat=lat, lon=lon, nx_hexagon=60,
        color_continuous_scale="Viridis", labels={"color": "Airbnb listings > 60", "frame": "Period"},
        opacity=0.5, min_count=60, height=500, zoom=10,
       show_original_data=True, original_data_marker=dict(opacity=0.5, size=3, color="grey"))
    #fig.update_layout(title={'text': "density spots 2D"})
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    #col1, col2 = st.beta_columns(2)
    #with col2:
    st.write('2D Map')
    st.plotly_chart(fig)

    # CREATING FUNCTION FOR MAPS

    def map(data, latitude, longitude):
        st.pydeck_chart(pdk.Deck( map_style="mapbox://styles/johnzinz/ckihdfwni4slu1atbeqiucn34",
            initial_view_state={
                "latitude": latitude,
                "longitude": longitude,
                "zoom": 10,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "GridLayer",
                    data=data,
                    opacity=0.2,
                    pickable=True,
                    extruded=True,
                    cell_size=100,
                    elevation_scale=2,
                    get_position=["longitude", "latitude"],
                ),
            ],
                     tooltip={"text": "{position}\nCount: {count}"},
                     mapbox_key='pk.eyJ1Ijoiam9obnppbnoiLCJhIjoiY2tmbWthazZ6MDNueDJxb2ZyZ2M3czU0dyJ9.Bl3T4kl14xan7glGxid_Rw'

        ))


    #with col1:
     #   st.write('3D Map #(press control to rotate map)')
        #map(df2,center[0], center[1])

