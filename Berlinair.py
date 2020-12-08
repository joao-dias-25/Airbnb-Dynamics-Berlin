import streamlit as st

import Page1
import Page2

st.set_page_config(layout="wide")

PAGES = {
    "Top 10 neighbourhoods": Page1,
    "Map": Page2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]


st.sidebar.markdown('---')


st.sidebar.image('uca-url.png', caption='Donation Address: bitcoin', width= 250)
#st.sidebar.image(Image.open('ethcode.jpeg'), caption='Donation Address: ethereum', width= 250)
page.app()

