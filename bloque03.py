# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 18:05:42 2024

@author: Daniel007
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

import warnings
warnings.filterwarnings("ignore")

database = pd.read_csv('database.csv')

# Crear un DataFrame de pandas
B3_0X = pd.DataFrame(database)

# Eliminar filas con propósitos NaN
B3_0X = B3_0X.dropna(subset=['Purpose'])

# Dividir la columna 'Purpose' en múltiples columnas para cada propósito
B3_0X['Purposes'] = B3_0X['Purpose'].apply(lambda x: str(x).split(','))
B3_0X = B3_0X.explode('Purposes')

# Crear un gráfico interactivo con Plotly
fig = px.bar(B3_0X, x='Country of Operator/Owner', color='Purposes', text='Official Name of Satellite',
             title='Number of Satellites by Purpose for Each Country of Operator/Owner',
             labels={'Country of Operator/Owner': 'Country of Operator/Owner', 'Purposes': 'Purpose'},
             category_orders={'Purposes': sorted(B3_0X['Purposes'].unique())},
             height=500)

# Personalizar el diseño
fig.update_layout(xaxis_title='Country of Operator/Owner', yaxis_title='Number of Satellites',
                  legend_title_text='Purpose', barmode='stack')

# Añadir interactividad al hacer clic en un país de operador/propietario
fig.update_traces(selector=dict(type='bar'), hoverinfo='y+name')

# Mostrar el gráfico interactivo en el navegador
fig.show()
B3_0X=fig