import streamlit as st
import pyqrcode
import Page1
import Page2

PAGES = {
    "Top 10 neighbourhoods": Page1,
    "Map": Page2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]




from PIL import Image
st.sidebar.image(Image.open('uca-url.png'), caption='Donation Address: bitcoin', width= 250)
#st.sidebar.image(Image.open('ethcode.jpeg'), caption='Donation Address: ethereum', width= 250)
page.app()

