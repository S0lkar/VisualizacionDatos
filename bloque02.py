import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from st_pages import add_page_title

# add to nav
add_page_title()

FILENAME = 'database.csv'
'''Official Name of Satellite,Country/Organization of UN Registry,Operator/Owner,Country of Operator/Owner,Users,Purpose,
Detailed Purpose,Class of Orbit,Type of Orbit,Longitude of Geosynchronous Orbit (Degrees),Perigee (Kilometers),
Apogee (Kilometers),Eccentricity,Inclination (Degrees),Period (Minutes),Launch Mass (Kilograms),Dry Mass (Kilograms),
Power (Watts),Date of Launch,Expected Lifetime (Years),Contractor,Country of Contractor,Launch Site,Launch Vehicle,COSPAR Number,NORAD Number'''


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

    st.write(f'<p style="color:#f4ebd0">{text_b201}</p>', unsafe_allow_html=True)
    st.plotly_chart(figure_or_data=B2_01(df), use_container_width=True)
    st.write(f'<p style="color:#f4ebd0">{text_b202}</p>', unsafe_allow_html=True)
    st.plotly_chart(figure_or_data=B2_02(df), use_container_width=True)
    return True


def B2_01(df):
    df['Date of Launch'] = pd.to_datetime(df['Date of Launch'])
    df['Year of Launch'] = df['Date of Launch'].apply(lambda x: x.year)
    count_year_df = df.groupby('Year of Launch')['Country of Operator/Owner'].count()
    newlegend = {'Country of Operator/Owner': 'Launches'}
    fig = px.bar(count_year_df, labels={'value': 'Number of launches'},
                 title='Launches of the current active satellites till 2016')
    fig.for_each_trace(lambda t: t.update(name=newlegend[t.name],
                                          legendgroup=newlegend[t.name],
                                          hovertemplate=t.hovertemplate.replace(t.name, newlegend[t.name])
                                          ))
    return fig


def B2_02(df):
    df_countries = df[df['Year of Launch'] > 1997]
    fig = px.pie(df_countries, names='Purpose', title='Active Satellites purposes till 2016')

    return fig


B2_Frontend()
