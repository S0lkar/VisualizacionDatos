# ---------- Modules ---------
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit.components.v1 as components
import folium
import altair as alt
import re
from st_pages import add_page_title
from scipy.constants import kilo
from numpy import radians
from orbital import earth, KeplerianElements, plot, earth_sidereal_day

# --------- Global variables ---------
FILENAME = 'database.csv'


# --------- Global functions ---------
def PositionImage(data, proportions = [0.15, 0.7, 0.15], usecol = 1):
    cols = st.columns(proportions)
    with cols[usecol]:
        st.plotly_chart(figure_or_data= data, use_container_width=True)
    pass

@st.cache_resource
def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
def add_audio(filename):
    audio_file = open(filename, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mpeg")