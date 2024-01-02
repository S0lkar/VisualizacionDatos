import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

FILENAME = 'database.csv'
'''Official Name of Satellite,Country/Organization of UN Registry,Operator/Owner,Country of Operator/Owner,Users,Purpose,
Detailed Purpose,Class of Orbit,Type of Orbit,Longitude of Geosynchronous Orbit (Degrees),Perigee (Kilometers),
Apogee (Kilometers),Eccentricity,Inclination (Degrees),Period (Minutes),Launch Mass (Kilograms),Dry Mass (Kilograms),
Power (Watts),Date of Launch,Expected Lifetime (Years),Contractor,Country of Contractor,Launch Site,Launch Vehicle,COSPAR Number,NORAD Number'''


def B2_Frontend():
    st.plotly_chart(figure_or_data=B2_01(), use_container_width=True)
    return True


def B2_01():
    df = pd.read_csv(FILENAME)
    df['Date of Launch'] = pd.to_datetime(df['Date of Launch'])
    df['Year of Launch'] = df['Date of Launch'].apply(lambda x: str(x.year))
    count_year_df = df.groupby('Year of Launch')['Country of Operator/Owner'].count()
    newlegend = {'Country of Operator/Owner': 'Launches'}
    fig = px.bar(count_year_df, labels={'value': 'Number of launches'},
                 title='Evolution of the number of satellite launches')
    fig.for_each_trace(lambda t: t.update(name=newlegend[t.name],
                                          legendgroup=newlegend[t.name],
                                          hovertemplate=t.hovertemplate.replace(t.name, newlegend[t.name])
                                          ))
    return fig
