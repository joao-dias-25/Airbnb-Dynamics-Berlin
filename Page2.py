import streamlit as st
import pandas as pd
import requests
from io import StringIO

def app():
    st.title('AirBnB in Berlin')
    st.write('Here you see that')

    DATA_URL = 'https://ndownloader.figshare.com/files/25533041'

    @st.cache(persist=True)
    def load_data():
        url = requests.get(DATA_URL)
        csv_raw = StringIO(url.text)
        data = pd.read_csv(csv_raw, low_memory=False,index_col=0)
        #data['date'] = pd.to_datetime(data['date'])
        return data

    df = load_data()


    import plotly.express as px
    import plotly.figure_factory as ff

    # it needs a token for access mapbox
    px.set_mapbox_access_token(
        'pk.eyJ1Ijoiam9obnppbnoiLCJhIjoiY2tmbWthazZ6MDNueDJxb2ZyZ2M3czU0dyJ9.Bl3T4kl14xan7glGxid_Rw')

    lat = df['latitude']
    lon = df['longitude']
    frame = df['date']

    fig = ff.create_hexbin_mapbox(
        lat=lat, lon=lon, nx_hexagon=60, animation_frame=frame,
        color_continuous_scale="Viridis", labels={"color": "Airbnb listings > 60", "frame": "Period"},
        opacity=0.5, min_count=60, height=500, zoom=10,
       show_original_data=True, original_data_marker=dict(opacity=0.4, size=3, color="grey"))
    fig.update_layout(title={'text': "density spots"})
    fig.update_layout(margin={"r": 0, "t": 30, "l": 0, "b": 0})

    st.plotly_chart(fig)

