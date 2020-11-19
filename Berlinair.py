import streamlit as st
import numpy as np
import pandas as pd

import Page1
import Page2

PAGES = {
    "Top 10 neighbourhoods": Page1,
    "Map": Page2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

