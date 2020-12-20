import streamlit as st
import requests
from io import StringIO
import pandas as pd

import Page1
import Page2
import Page3

st.set_page_config(layout="wide")

PAGES = {
    "Top neighbourhoods": Page1,
    "Map": Page2,
    "neighbourhood price": Page3
}
st.sidebar.title('Navigation')
city = st.sidebar.radio("City", ['Berlin','Porto'])

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]



st.sidebar.markdown('---')


st.sidebar.image('uca-url.png', caption='Donation Address: bitcoin', width= 250)
#st.sidebar.image(Image.open('ethcode.jpeg'), caption='Donation Address: ethereum', width= 250)

st.title(f'AirBnB in {city}')

my_cities = {'Berlin': 'https://ndownloader.figshare.com/files/25844933',
             'Porto': 'https://ndownloader.figshare.com/files/25846991'}

my_geojson = {'Berlin': 'berlin-neighbourhoods.geojson',
             'Porto': 'Porto-neighbourhoods.geojson'}
my_last_date = {'Berlin': '2020-10-13',
             'Porto': '2020-11-08'}

DATA_URL = my_cities.get(city)
geojson_string = my_geojson.get(city)
last_date = my_last_date.get(city)
#'https://ndownloader.figshare.com/files/25767323'


@st.cache(persist=True,allow_output_mutation=True)
def load_data():
    url = requests.get(DATA_URL).content
    csv_raw = StringIO(url.decode('utf-8'))
    data = pd.read_csv(csv_raw, low_memory=False, index_col=0)
    # data['date'] = pd.to_datetime(data['date'])
    return data

#loads the data for every page
page.app(load_data(),geojson_string,last_date)

