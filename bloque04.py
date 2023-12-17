
# ------- Módulos para tratar los datos -------
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from numpy import radians
import pandas as pd
import streamlit as st
# pip install orbitalpy -> orbital.__file__ -> arreglos de tipado
from orbital import earth, KeplerianElements, plot, earth_sidereal_day
import streamlit.components.v1 as components
from scipy.constants import kilo


# ------- Variables Globales -------
FILENAME = 'database.csv' # El nombre de nuestra base de datos


# ------- Funciones de visualización -------
# Todas estas funciones devuelven las gráficas que luego se imprimen en streamlit
Elliptical = KeplerianElements.with_period(earth_sidereal_day / 2, e=0.741, i=radians(63.4), arg_pe=radians(270), body=earth)
GEO = KeplerianElements.with_altitude(4000 * kilo, body=earth)
MEO = KeplerianElements.with_altitude(1000 * kilo, body=earth)
LEO = KeplerianElements.with_altitude(300 * kilo, body=earth)

def B4_Frontend():
    audio_file = open("audio/intro.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mpeg")
    st.subheader("| ¿Qué clases de órbitas existen?")
    st.write("LEO")
    ani = plot(LEO, title='Órbita LEO', animate=True)
    components.html(ani.to_jshtml(), height=600)
    plt.clf()
    st.write("MEO")
    ani = plot(MEO, title='Órbita MEO', animate=True)
    components.html(ani.to_jshtml(), height=600)
    plt.clf()
    st.write("GEO")
    ani = plot(GEO, title='Órbita GEO', animate=True)
    components.html(ani.to_jshtml(), height=600)
    plt.clf()
    st.write("Elliptical")
    ani = plot(Elliptical, title='Órbita Elíptica', animate=True)
    components.html(ani.to_jshtml(), height=600)
    plt.clf()
    
    st.write("En la actualidad, la distribución de los satélites activos según la clase de órbita es la que sigue:")
    st.pyplot(B4_01())
    st.subheader("| ¿Qué tipos de órbita existen?")
    st.write('Según el ámbito de uso del satélite, se colocan en un tipo de órbita u otro. Por ejemplo, a la hora de tomar fotos en ciertos lugares siempre a la misma hora se colocará el satélite en una órbita heliosíncrona. Los tipos principales son Ecuatorial, Non-Polar Inclined, Polar, Elíptica, Deep Highly Eccentric, Molniya, y Cislunar')
    st.write('La distribución de los satélites en los diferentes tipos de órbita es la siguiente:')
    st.pyplot(B4_02())
    return
    
# TODO: Diseñar el aspecto según el fondo que se elija finalmente
def B4_01():
    DF = pd.read_csv(FILENAME)
    fig, ax = plt.subplots()
    DF['Class of Orbit'].replace('LEO ', 'LEO', inplace=True) # Hay un dato mal nombrado, con un espacio de más.
    cuentas = DF['Class of Orbit'].value_counts()
    ax.bar('LEO', height=cuentas[0], label='LEO')
    ax.bar('GEO', height=cuentas[1], label='GEO')
    ax.bar('MEO', height=cuentas[2], label='MEO')
    ax.bar('Elliptical', height=cuentas[3], label='Elíptica')
    return plt.gcf()

# TODO: Diseñar el aspecto según el fondo que se elija finalmente
def B4_02():
    DF = pd.read_csv(FILENAME)
    fig, ax = plt.subplots()
    cuentas = DF['Type of Orbit'].value_counts()
    nombres = DF['Type of Orbit'].unique()
    w = 0.75
    ax.bar(nombres[0], height=cuentas[0], label=nombres[0], width=w)
    ax.bar(nombres[3], height=cuentas[1], label=nombres[3], width=w)
    ax.bar(nombres[4], height=cuentas[2], label=nombres[4], width=w)
    ax.bar(nombres[2], height=cuentas[3], label=nombres[2], width=w)
    ax.bar(nombres[-2], height=cuentas[4], label=nombres[-2], width=w)
    ax.bar(nombres[5], height=cuentas[5], label=nombres[5], width=w)
    ax.bar(nombres[6], height=cuentas[6], label=nombres[6], width=w)
    ax.bar(nombres[-1], height=cuentas[7], label=nombres[-1], width=w)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right" )
    plt.show()
    
    return plt.gcf()

