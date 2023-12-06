
'''
> Código relacionado únicamente con la parte visual

'''

# ------- Módulos para traer las gráficas a streamlit -------
import streamlit as st
import figure_manager as fm
import matplotlib.pyplot as plt

# ------- Variables Globales -------
# Ninguna de momento

 
# ------- Contenido de la página -------
# Aquí se dan las instrucciones para montar la página (definiendo el estilo, gráficas...)
st.pyplot(fm.Vis1())
st.pyplot(fm.Vis2())