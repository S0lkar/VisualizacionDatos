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
    estratégico del espacio exterior.\n La competición, que concluyó en 1975 con el acople de la nave Apolo-Soyuz, 
    se extendería durante más de dos décadas en las que se sucederían algunos de los logros tecnológicos más importantes
    jamás alcanzados por ambas potencias.'''

    text_b202 = '''Desde 1997 podemos observar un claro incremento del número de lanzamientos. Impulsado en su mayor
    parte por los avances tecnológicos y el creciente auge de las comunicaciones en este siglo.'''

    st.write(text_b201, unsafe_allow_html=True)
    PositionImage(B2_01(df))
    st.write(text_b202, unsafe_allow_html=True)
    PositionImage(B2_02(df))
    return True


def B2_01(df):
    # fig = px.bar(df['Country/Organization of UN Registry'].value_counts().sort_values(ascending=False), labels={'value': 'País/Organización'},
    #              title='Country/Organization of UN Registry')
    df_a = df['Country/Organization of UN Registry'].value_counts()

    #df_a = df_a.where(df_a >= 29)
    #df_a.loc[df_a < 29] = 'Other countries'

    fig = px.pie(df, values=df_a.values, names=df_a.index,
                 title='Número de satélites activos registrados ante la ONU por país')
    #fig.update_layout(yaxis={'categoryorder': 'total descending'})
    # fig.for_each_trace(lambda t: t.update(name=newlegend[t.name],
    #                                       legendgroup=newlegend[t.name],
    #                                       hovertemplate=t.hovertemplate.replace(t.name, newlegend[t.name])
    #                                       ))
    return fig


def B2_02(df):
    fig = px.pie(df, names=df['Country of Operator/Owner'], title='Número de satélites activos por país')

    return fig


B2_Frontend()
