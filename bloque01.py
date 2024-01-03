# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:02:22 2023

@author: Raquel
"""

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#-----------DATOS-------------
FILENAME = 'database.csv'
global DF
global boton2 
boton2=False


#Código que luego va al Streamlit
def B1_Frontend():
    
    global boton2
       
    
    #Pongo el audio por que he visto que está en todas las pestañas
    audio_file = open("audio/intro.mp3","rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mpeg")
   
    #Título para captar la atención
    #st.header("¿Quieres saber qué nos dicen los datos de la industria de los cohetes?")
    
   
        
    st.markdown('<h1 style="text-align: center; margin-top: 300px; color: white;">¿Quieres saber qué nos dicen los datos de la industria de los cohetes?</h1>', unsafe_allow_html=True)
    
    #Botón para continuar con la información. 
    boton = st.button("Pincha aquí", type="primary")
    #boton = st.markdown('<div class="center"><button style="background-color: #69bfdb; color:white; padding: 15px 35px; border:white; cursor:pointer;">Pincha aquí</button></div>', unsafe_allow_html=True)

   
    #Si se pulsa se muestra la gráfica
    if boton:
         
        st.markdown('<h2 style="text-align: center; color: #316633;"><span style="font-size: 77px;">xxx%</span> <span style="font-size: 30px;">lanzamientos mas</span></h2>', unsafe_allow_html=True)
        #st.markdown('<h2 style="text-align: center; color: #316633; font-size: 55px">xxx% lanzamientos mas</h2>',unsafe_allow_html=True)
        #st.header("Crecimiento de 17300% en el lanzamiento de cohetes ")
        st.pyplot(B1_01())
        st.markdown('<h2 style="text-align: center;">El avance tecnológico también se refleja en el tiempo de vida de los satélites</h2>',unsafe_allow_html=True)
        #st.subheader("El avance tecnológico también queda reflejado en el tiempo de vida de los satélites")
        st.pyplot(B1_02())
        
        #st.subheader("Es coherente pensar que de primeras...")
        #st.image('./imgs/esquema_bloque1.jpg')
        #las tres flechas de implicaciones
        boton2 = st.button("Pincha aquí para saber las consecuencias", type="primary")
        
        st.markdown('<h1 style="color: red;">PROBLEMA</h1>', unsafe_allow_html=True)

        
        #st.header("PROBLEMA:")
        st.markdown('<h2 style="text-align: center;">Crecimiento exponencial en la acumulación de basura espacial</h2>',unsafe_allow_html=True)
        #st.subheader("Crecimiento exponencial en la acumulación de basura espacial")
        st.pyplot(B1_03())
            
           
    return
           
           
        # Poner las tres flechas de implicaciones y la gráfica de acumulación
        #st.pyplot(B1_03())
        
        
        
 
def B1_01():
    
    FILENAME= 'database.csv'
    data = pd.read_csv(FILENAME)
    global DF

    #Paso a fecha
    date_launch = pd.to_datetime(data["Date of Launch"])
    #Me quedo con el año y quito los 4 valores nulos
    date_year = (date_launch.dt.year).dropna()

    age=np.arange(1992,2016,dtype=int)
    cuentas = date_year.value_counts()
    #Hay algunos años que no existen lanzamientos, necesito rellenar con 0
    #Completo todas las frecuencias en la lista
    frecuencias=[]
    for year in age:
        if year in cuentas.index:
            freq = cuentas.loc[year]
            
        else:
            freq = 0
            
        frecuencias.append(freq)
        
    #Creo dataframe con todos los años y las frecuencias
    DF = pd.DataFrame({'Año': age, 'Frecuencia':frecuencias})


    #Visualización
    fig,ax=plt.subplots()
    plt.plot(DF['Año'],DF['Frecuencia'],marker='o',linestyle='--',linewidth= 1.5,color='green')
    ax.set_xlabel('Año',fontsize=14)
    ax.set_ylabel('Número de lanzamientos',fontsize=14)
    #:ax.set_title('Evolución del número de lanzamientos por año')


    plt.ylim(0,180)
    plt.yticks(fontsize=9)
    plt.xticks(age[::3],age[::3])
    
       
    return fig   
        
def B1_02():
    data = pd.read_csv(FILENAME)

    df= data[["Date of Launch","Expected Lifetime (Years)"]]
    #Convierto a fecha y me quedo con los años
    df.loc[:,"Date of Launch"]=pd.to_datetime(df["Date of Launch"]).dt.year
    #Ordeno cronológicamente
    df=df.sort_values(by="Date of Launch")
    #Suprimo los valores nulos
    df = df.dropna(axis=0)
    df = df.drop(df.index[-1])

    #Time life del primer año (menos avance tecnológico)
    año_menor, tl_menor = df.iloc[0,:]
    #Time life del último satélite mandado (mayor avance tecnológico)
    año_mayor, tl_mayor = df.iloc[-1,:]
    
    años = [año_menor, año_mayor]
    tl = [tl_menor,tl_mayor]
   
    #Visualización
    fig,ax = plt.subplots()
    ax.bar(0,height=tl_menor,label=str(año_menor),width=0.5, align="center")
    ax.bar(1, height=tl_mayor, label= str(año_mayor), width=0.5, align="center")
    ax.set_xticks([0,1])
    ax.set_xticklabels([str(int(año_menor)), str(int(año_mayor))])
    ax.set_xlabel("Años")
    
    ax.set_ylabel("Tiempo de vida esperado en años")
   
    
    ax.set_ylim(0,16)
    #st.pyplot(B1_02())
    return fig

def B1_03():
    acumulated_satelites = DF["Frecuencia"].cumsum()
    
    fig,ax = plt.subplots()
    acumulated_satelites.plot(kind = 'line', linestyle = '-')
    plt.scatter(DF["Año"], acumulated_satelites, linewidths=1)
    ax.set_xlabel("Año")
    ax.set_ylabel("Satélites en el espacio")
    plt.ylim(0,1400)
    plt.xlim(1990,2015)
    
    
    #GRÁFICO DE AREA COLOREADA
    # fig, ax = plt.subplots()
    
    # # Dibujar el área bajo la curva
    # ax.fill_between(DF["Año"], acumulated_satelites, color='skyblue', alpha=0.4)
    
    # # Dibujar la línea
    # ax.plot(DF["Año"], acumulated_satelites, color='blue', alpha=0.6)
    
    # # Configurar ejes y etiquetas
    # ax.set_xlabel("Año")
    # ax.set_ylabel("Satélites en el espacio")
    # plt.ylim(0, 1400)
    # plt.xlim(1990, 2015)
    
    
    return fig