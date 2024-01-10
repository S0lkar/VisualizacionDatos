# ------- Módulos para tratar los datos -------
import matplotlib.pyplot as plt
from numpy import radians
import pandas as pd
import streamlit as st
from orbital import earth, KeplerianElements, plot, earth_sidereal_day
import streamlit.components.v1 as components
from scipy.constants import kilo
import plotly.express as px
# Fuente de información: https://www.esa.int/Enabling_Support/Space_Transportation/Types_of_orbits
from st_pages import add_page_title

# add to nav
add_page_title()

# ------- Variables Globales -------
FILENAME = 'database.csv'  # El nombre de nuestra base de datos
DF = pd.read_csv(FILENAME)

# ------- Funciones de visualización -------
# Todas estas funciones devuelven las gráficas que luego se imprimen en streamlit
Elliptical = KeplerianElements.with_period(earth_sidereal_day / 2, e=0.741, i=radians(63.4), arg_pe=radians(270),
                                           body=earth)
GEO = KeplerianElements.with_altitude(4000 * kilo, body=earth)
MEO = KeplerianElements.with_altitude(1000 * kilo, body=earth)
LEO = KeplerianElements.with_altitude(300 * kilo, body=earth)


def PositionImage(data, proportions=[0.15, 0.7, 0.15], usecol=1):
    cols = st.columns(proportions)
    with cols[usecol]:
        st.plotly_chart(figure_or_data=data, use_container_width=True)
    pass


# TODO: Diseñar el aspecto según el fondo que se elija finalmente
def B4_01():
    global DF
    DF['Class of Orbit'].replace('LEO ', 'LEO', inplace=True)  # Hay un dato mal nombrado, con un espacio de más.
    count_orbit_df = DF.groupby('Class of Orbit')['Class of Orbit'].count()
    fig = px.bar(count_orbit_df, labels={'value': 'Número de satélites', 'index': 'Clase de órbita'},
                 title='Número de satélites por clase de órbita')
    return fig


def B4_02():
    global DF
    count_orbit_df = DF.groupby('Type of Orbit')['Type of Orbit'].count()
    fig = px.bar(count_orbit_df, labels={'value': 'Número de satélites', 'index': 'Tipo de órbita'},
                 title='Número de satélites por tipo de órbita')
    return fig


# ------- Apariencia del bloque -------
def B4_Frontend():
    audio_file = open("audio/intro.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mpeg")
    st.subheader("| ¿Qué clases de órbitas existen?")
    st.write(
        "Decimos que una órbita pertenece a una clase u otra en función de su <b>distancia respecto a la Tierra </b>. En esta clasificación sólo es reletante la distancia y la forma.")
    st.write("<h3>LEO</h3>", unsafe_allow_html=True)
    st.write(
        "LEO (<i>Low Earth Orbit</i>) es la órbita con menor distancia a la tierra, en un rango de 160 a 700kms de radio. "
        "Generalmente este tipo de satélites se utilizan para tomar imágenes (al estar cercanas a la tierra las imágenes son de alta resolución) "
        " y al estar cerca de la Estación Espacial Internacional, es relativamente sencillo viajar a los satélites."
        " Este tipo de satélites alcanzan hasta 7.8 kms/s, lo que les permite dar una vuelta a la Tierra en ~90 minutos.",
        unsafe_allow_html=True)
    ani = plot(LEO, title='Órbita LEO', animate=True)
    components.html(ani.to_jshtml(), height=600)
    plt.clf()
    st.write("<h3>MEO</h3>", unsafe_allow_html=True)
    st.write(
        "MEO (<i>Medium Earth Orbit</i>) es una órbita generalmente con un radio más amplio que la LEO y con <i>mayor diversidad en la orientación</i>. MEO abarca órbitas de 500 a 1000kms de radio. "
        "Este tipo de órbita se utilizan para satélites de todo tipo. Una de las funciones más llamativas son los sistemas de navegación, "
        " como European Galileo System, utilizado en la comunicación europea."
        " Como se aprecia en la animación, su periodo es ligeramente más lento que el de LEO por la diferencia en radio.",
        unsafe_allow_html=True)
    ani = plot(MEO, title='Órbita MEO', animate=True)
    components.html(ani.to_jshtml(), height=600)
    plt.clf()
    st.write("<h3>GEO</h3>", unsafe_allow_html=True)
    st.write(
        "GEO (<i>Geostationary Orbit</i>) es una órbita con el radio más amplio entre LEO y MEO, con un periodo de 23 horas 56 minutos y 4 segundos. "
        "Debido a su periodo igual al tiempo de rotación de la Tierra, se le dio el nombre de 'geoestacionario' ya que con respecto a la tierra siempre se encuentra en la misma posición."
        " El uso fundamental de los satélites de esta órbita es la telecomunicación"
        " como European Galileo System, utilizado en la comunicación europea."
        " Como se aprecia en la animación, su periodo es mucho más lento que el de LEO y MEO por la diferencia en radio.",
        unsafe_allow_html=True)
    ani = plot(GEO, title='Órbita GEO', animate=True)
    components.html(ani.to_jshtml(), height=600)
    plt.clf()
    st.write("<h3>Elliptical</h3>", unsafe_allow_html=True)
    st.write(
        "Las órbitas elípticas se utilizan para satélites muy especializados y fuera de los ámbitos más comunes como telecomunicaciones y navegación. "
        "Los cálculos de su periodo y velocidad son más dificiles de tratar debido a que la velocidad no permanece constante en el tiempo; "
        "a mayor cercanía con la Tierra mayor es la influencia de la gravedad, con lo que existe un incrementeo de la aceleración que afecta a los satélites. "
        "En la siguiente animación se puede apreciar dicho incremento y su irregularidad.", unsafe_allow_html=True)
    ani = plot(Elliptical, title='Órbita Elíptica', animate=True)
    components.html(ani.to_jshtml(), height=600)
    plt.clf()

    st.write("En la actualidad, la distribución de los satélites activos según la clase de órbita es la que sigue:")
    PositionImage(B4_01())
    st.subheader("| ¿Qué tipos de órbita existen?")
    st.write(
        'Según el ámbito de uso del satélite, se colocan en un tipo de órbita u otro. Por ejemplo, a la hora de tomar fotos en ciertos lugares siempre a la misma hora se colocará el satélite en una órbita heliosíncrona. Los tipos principales son Ecuatorial, Non-Polar Inclined, Polar, Elíptica, Deep Highly Eccentric, Molniya, y Cislunar')
    st.write('La distribución de los satélites en los diferentes tipos de órbita es la siguiente:')
    PositionImage(B4_02())
    return


B4_Frontend()
