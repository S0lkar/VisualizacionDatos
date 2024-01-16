# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 18:05:42 2024

@author: Daniel007
"""

from CommonTools import *

# add to nav
add_page_title(initial_sidebar_state="expanded", layout="wide")
local_css("frontend.css")

database = pd.read_csv('database.csv')
 

def B1_Frontend():
    
    st.write('''Tomando aquellos países que poseen más de 20 satélites para ver aquellos con mayor poder en ingeniería aeroespacial,se observa que estos son USA, Alemania, Canadá, China, Japón, Rusia, India y Reino Unido, además de otros lanzados de manera multinacional y la Agencia Espacial Europea.
    Se puede observar fácilmente que el país que más destaca es USA por tener la mayor cantidad y variedad de satélites en órbita. Los dos únicos países que pueden mínimamente compararse con el poderío espacial de Estados Unidos son China y Rusia (especialmente China hoy en día).
    El mayor uso que se demuestra son para comunicaciones, seguido de observación de la Tierra y desarrollo tecnológico.''')

    st.write("\n")
    st.write('''El motivo de que destaque el uso de satélites en comunicaciones se explica por la utilización de teléfono móviles, internet, canales de televisión, radio y uso militar. 🚀🚀''')

    st.write("\n")
    st.write('''El motivo del gran uso también de satélites de observación de la Tierra son sobretodo por motivos de información meteorológica y geográfica. 🚀🚀''')

    fig=B3_01()
    PositionImage(fig)


def B3_01():
    # Crear un DataFrame de pandas
    B3_0X = pd.DataFrame(database)
    
    # Eliminar filas con propósitos NaN
    B3_0X = B3_0X.dropna(subset=['Purpose'])
    
    # Dividir la columna 'Purpose' en múltiples columnas para cada propósito
    B3_0X['Purposes'] = B3_0X['Purpose'].apply(lambda x: str(x).split(','))
    B3_0X = B3_0X.explode('Purposes')
    
    # Filtrar países con más de 20 satélites
    countries_with_more_than_20_satellites = B3_0X['Country of Operator/Owner'].value_counts()[B3_0X['Country of Operator/Owner'].value_counts() > 20].index
    B3_0X_filtered = B3_0X[B3_0X['Country of Operator/Owner'].isin(countries_with_more_than_20_satellites)]
    
    # Crear un gráfico interactivo con Plotly
    B3_0X = px.bar(B3_0X_filtered, x='Country of Operator/Owner', color='Purposes', text='Official Name of Satellite',
                 title='Número de satélites por propósito para cada país de operador/propietario (países con >20 satélites)',
                 labels={'Country of Operator/Owner': 'Country of Operator/Owner', 'Purposes': 'Purpose'},
                 category_orders={'Purposes': sorted(B3_0X_filtered['Purposes'].unique())},
                 height=500)
    
    # Personalizar el diseño
    B3_0X.update_layout(xaxis_title='País del operador/propietario', yaxis_title='Número de satélites',
                      legend_title_text='Objetivo', barmode='stack')
    
    # Añadir interactividad al hacer clic en un país de operador/propietario
    B3_0X.update_traces(selector=dict(type='bar'), hoverinfo='y+name')
    
    return B3_0X

B1_Frontend()