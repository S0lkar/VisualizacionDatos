import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from st_pages import add_page_title
from CommonTools import *

# add to nav
add_page_title(initial_sidebar_state="expanded", layout="wide")
local_css("frontend.css")

FILENAME = 'database.csv'

def B2_Frontend():
    # Cargamos el csv
    df = pd.read_csv(FILENAME)

    text_b201 = '''El lanzamiento del satélite artificial Sputnik-1 el 4 de octubre de 1957 por parte de la Unión 
    Soviética, el primer satélite en la historia en alcanzar la órbita terrestre, 
    daría lugar al comienzo de lo que se conoció como la Carrera Espacial, que en el contexto de la Guerra Fría puede 
    entenderse como la carrera armamentística en la que americanos y soviéticos se disputaron el control 
    estratégico del espacio exterior.
    La competición, que concluyó en 1975 con el acople de la nave Apolo-Soyuz, 
    se extendería durante más de dos décadas en las que se sucederían algunos de los logros tecnológicos más importantes
    jamás alcanzados por ambas potencias.'''
    text_b202 = '''Esta competición hizo que el principal propósito de la Convención de 1976 para el registro de lanzamiento de
    objetos al espacio exterior fuera conseguir transparencia en las actividades espaciales y comenzar una regulación
    internacional del uso y exploración del espacio exterior. Sin embargo el carácter no vinculante de las resoluciones
    acerca de este aspecto provocan que bien por errores adminsitrativos, por poca atención
    de los países o por ocultar nuevas tecnologías de ámbito militar haya muchos satélites sin registrar.'''

    text_b203 = '''Desde 1997 podemos observar un claro incremento del número de lanzamientos. Impulsado en su mayor
    parte por los avances tecnológicos y el creciente auge de las comunicaciones en este siglo.'''

    text_b204 = '''Como podemos observar en el gráfico también se disputa la hegemonía mundial en el terreno espacial,
    ya que Estados Unidos, Rusia y China conforman el podio de los países con más satélites en órbita'''

    st.write(text_b201, unsafe_allow_html=True)
    st.write(text_b202, unsafe_allow_html=True)
    PositionImage(B2_01(df))
    st.write(text_b203, unsafe_allow_html=True)
    st.write(text_b204, unsafe_allow_html=True)
    PositionImage(B2_02(df))
    
    return True


def B2_01(df):
    # fig = px.bar(df['Country/Organization of UN Registry'].value_counts().sort_values(ascending=False), labels={'value': 'País/Organización'},
    #              title='Country/Organization of UN Registry')

    def setOtherCountry(s):
        s = 'Other countries'
        return s

    df_a = df['Country/Organization of UN Registry'].value_counts()
    df_b = df['Country/Organization of UN Registry'].value_counts()

    df_a = df_a.where(df_a >= 29)
    df_b = df_b.where(df_b < 29).rename(setOtherCountry, axis=0)
 
    df_c = pd.concat([df_a,df_b])

    fig = px.pie(df_c, values=df_c.values, names=df_c.index,
                 title='Número de satélites activos registrados ante la ONU por país')
    #fig.update_layout(yaxis={'categoryorder': 'total descending'})
    # fig.for_each_trace(lambda t: t.update(name=newlegend[t.name],
    #                                       legendgroup=newlegend[t.name],
    #                                       hovertemplate=t.hovertemplate.replace(t.name, newlegend[t.name])
    #                                       ))
    return fig


def B2_02(df):
    def setOtherCountry(s):
        s = 'Other countries'
        return s
    df_a = df['Country of Operator/Owner'].value_counts()
    df_b = df['Country of Operator/Owner'].value_counts()
    df_a = df_a.where(df_a >= 33)
    df_b = df_b.where(df_b < 33).rename(setOtherCountry, axis=0)
 
    df_c = pd.concat([df_a,df_b])
    fig = px.pie(df_c, names=df_c.index, values=df_c.values, title='Número de satélites activos en 2016 por país')

    return fig


B2_Frontend()
