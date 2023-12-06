
'''
> Aquí está el código relacionado con los datos/creación de gráficas

'''

# ------- Módulos para tratar los datos -------
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ------- Variables Globales -------
FILENAME = 'nose.csv' # El nombre de nuestra base de datos
# podriamos hacerlo Dataframe y tenerlo en global para todas las funciones...

# ------- Funciones Base -------
# Si queremos tener funciones en común para tratar el dataframe, etc...


# ------- Funciones de visualización -------
# Todas estas funciones devuelven las gráficas que luego se imprimen en streamlit

def Vis1():
    #df = pd.read_csv(FILENAME) # Deberíamos de leer los datos y sacar qué se debe visualizar
    
    data = sns.load_dataset("iris") # lorem ipsum básicamente
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
    
    return plt.gcf() # La función devuelve la figura tal y como se mostrará luego en streamlit

def Vis2():
    #df = pd.read_csv(FILENAME)
    data = sns.load_dataset("iris")
    
    
    # Pruebecillas para cosas mas complejas
    sns.set_palette('vlag') 
    plt.subplot(211) 
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)  
    sns.set_palette('Accent') 
    plt.subplot(212)
    sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
    
    return plt.gcf()