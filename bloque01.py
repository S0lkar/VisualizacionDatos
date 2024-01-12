from CommonTools import *
# add to nav
add_page_title(initial_sidebar_state="expanded", layout="wide")
local_css("frontend.css")

def B1_Frontend():
    titulo = st.empty()

    titulo.markdown(
        '<h1 style="text-align: center; margin-top: 300px;">¿Quieres saber qué nos dicen los datos de la industria de los satélites?</h1>',
        unsafe_allow_html=True)

    window = st.radio("", ["***DATOS***", "***CONSECUENCIAS***"], index=None, horizontal=True)

    if window == '***DATOS***':
        st.title("Crecimiento en el lanzamiento de cohetes")
        st.write(""" Desde los años 50 hemos incrementado exponencialmente el número de satélites lanzados🚀🚀""") 
            
        st.write("""Con el paso de los años cada vez es mayor nuestra evolución tecnológica en comunicación, meteorología, recogidas de datos, necesidad de investigación del espacio exterior...""")

        fig1 = B1_01()
        PositionImage(fig1)
        st.write("\n\n")
       
        st.title("¿Cuántos años de vida esperados tienen los satélites?")
        appointment = st.slider("Señala la fecha en las que estés interesado y descubre el ritmo de crecimiento: ", min_value=1978, max_value=1998,
                                value=1980)
        msg = B1_02(appointment)
        st.subheader("{} - lanzamiento de satélites con {} años de vida".format(appointment, msg))
        # text = "<div style='text-align: center;'>{} - {} años de vida</div>".format(appointment, msg)
        # st.markdown(text, unsafe_allow_html=True)
        st.write("Hay que destacar que estos son los años teóricos para los que está diseñado, los datos nos muestran que existen muchos casos en los que los satélites siguen ejerciendo su función muchos mas años de los esperados. Contrasta la información de ambas gráficas y aprecia cómo incluso doblan el número de años previstos.")

    if window == '***CONSECUENCIAS***':
        # st.subheader("La basura espacial se ha multiplicado por 5 en los últimos 10 años")
        #st.markdown(
        #    f"""
        #    <div style="text-align:center; color:orange; font-size:38px; padding:10px;">
        #    La basura espacial se ha multiplicado por 5 en los últimos 10 años
        #    </div>""", unsafe_allow_html=True)
        st.title("Acumulación desmesurdad de basura espacial")
        #st.title("El crecimiento exponencial en el lanzamiento de cohete a conducido a una QUINTUPLICACIÓN de la basura espacial en los últimos 10 AÑOS")
        st.write("""<p style='color:black;font-size:20px;font-weight:bold;'>EL crecimiento exponencial en el lanzamiento de cohetes ha conducido a una <span style='color:darkred;'>QUINTUPLICACIÓN</span> de la basura espacial en los últimos <span style='color:darkred;'>10 AÑOS</span>. ¡¡Observa cómo crece!!</p>""", unsafe_allow_html=True)

        fig = B1_03()
        PositionImage(fig)
        
        st.title("¿Qué efectos negativos trae la basura espacial?")
        st.write(""" Todos los satélites que se lanzan pasan a ser basura espacial. El riesgo de la basura espacial reside las velocidades a las que se desplaza en el espacio y el peligro que supone el impacto de ella contra satélites que están desarrollando su función o, en el peor de los casos, a misiones tripuladas. """)
        st.subheader("")
        st.image('./imgs/basura_espacial_bloque1.jpg')


def B1_01():
    data = pd.read_csv(FILENAME)
    # Paso a fecha
    data.loc[:, "Date of Launch"] = pd.to_datetime(data["Date of Launch"]).dt.year
    # Me quedo con el año y quito los 4 valores nulos
    df = pd.DataFrame(data["Date of Launch"])
    df = df.dropna()

    age = np.arange(1974, 2016, dtype=int)
    df_por_año = df["Date of Launch"].value_counts().sort_index()
    df_por_año = df_por_año.reindex(age, fill_value=0).reset_index()

    # Visualización
    fig = px.line(df_por_año, x="Date of Launch", y="count",
                  labels={"Date of Launch": "Año de Lanzamiento", "count": "Número de lanzamientos"},
                  title='Número de lanzamientos')
    return fig


def B1_02(appointment):
    data = pd.read_csv(FILENAME)
    df = data[["Date of Launch", "Expected Lifetime (Years)"]]
    df.loc[:, "Date of Launch"] = pd.to_datetime(df["Date of Launch"]).dt.year
    # Ordeno en orden cronológico
    df_orden = df.dropna(axis=0).sort_values(by="Date of Launch")
    # Reseteo los índices
    df_orden = df_orden.reset_index(drop=True)
    # Suprimo los caracteres no numéricos
    cleaned_val = []

    # Suprimo los valores que no son números ni guiones
    for val in df_orden["Expected Lifetime (Years)"]:
        cleaned = re.sub(r'[^0-9.-]', '', val)
        cleaned_val.append(cleaned)
    # Suprimo los intervalos y los sutituyo por el valor medio
    cleaned_val_out_intervals = []

    for val2 in cleaned_val:
        if '-' in val2:
            parts = val2.split('-')
            val = (float(parts[0]) + float(parts[1])) / 2
            cleaned_val_out_intervals.append(val)

        else:
            cleaned_val_out_intervals.append(float(val2))

    cleaned_df = pd.DataFrame({"Cleaned_Values": cleaned_val_out_intervals})
    result = pd.concat([df_orden["Date of Launch"], cleaned_df], axis=1)
    max_year = result.groupby('Date of Launch')['Cleaned_Values'].max()
    df_final = max_year.reset_index()
    df_final.columns = ['Años', 'Timelife']
    df_final['Años'] = df_final['Años'].astype(int)
    todos_los_años = list(range(1978, 2016 + 1))  # Crear una lista con todos los años
    df_final = df_final.set_index('Años').reindex(todos_los_años).fillna(0).reset_index()

    # Corto por el appointment
    df_cortado = df_final[df_final['Años'] <= appointment]
    msg = df_cortado["Timelife"].max()

    return msg


def B1_03():
    data = pd.read_csv(FILENAME)
    # Paso a fecha
    date_launch = pd.to_datetime(data["Date of Launch"])
    # Me quedo con el año y quito los 4 valores nulos
    date_year = (date_launch.dt.year).dropna()

    age = np.arange(1974, 2016, dtype=int)
    cuentas = date_year.value_counts()
    # Hay algunos años que no existen lanzamientos, necesito rellenar con 0
    df_frecuencias = cuentas.reindex(age, fill_value=0).reset_index()
    # Renombro las columnas
    df_frecuencias = df_frecuencias.rename(columns={'count': 'Frecuencia'})
    # Calculo la cumulación
    df_frecuencias["Frecuencia Acum"] = df_frecuencias["Frecuencia"].cumsum()
    # Represento gráficamente
    fig = px.bar(df_frecuencias, x='Date of Launch', y='Frecuencia Acum',
                 labels={"Date of Launch": "Año", "Frecuencia Acum": "Acumulación"}, title='Acumulación de satélites')

    return fig


B1_Frontend()
