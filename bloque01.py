from CommonTools import *
# add to nav
add_page_title(initial_sidebar_state="expanded", layout="wide")
local_css("frontend.css")

def B1_Frontend():
    titulo = st.empty()

    titulo.markdown(
        '<h1 style="text-align: center; margin-top: 300px; color: white;">¿Quieres saber qué nos dicen los datos de la industria de los satélites?</h1>',
        unsafe_allow_html=True)

    window = st.radio("", ["***DATOS***", "***CONSECUENCIAS***"], index=None, horizontal=True)

    if window == '***DATOS***':
        st.subheader(
            "Desde los años 50 el ser humano ha incrementado exponencialmente el número de satélites lanzados. Con el paso de los años cada vez es mayor nuestra evolución tecnológica en comunicación, meteorología, recogidas de datos, necesidad de investigación del espacio exterior...")
        fig1 = B1_01()
        PositionImage(fig1)
        st.write("\n\n")
        st.subheader(
            "Este avance tecnológico también queda reflejado en el crecimiento del tiempo de vida de los satélites lanzandos:")
        appointment = st.slider("Marque la fecha en la que esté interesado: ", min_value=1978, max_value=1998,
                                value=1980)
        msg = B1_02(appointment)
        st.subheader("{} - satélites con {} años de vida".format(appointment, msg))
        # text = "<div style='text-align: center;'>{} - {} años de vida</div>".format(appointment, msg)
        # st.markdown(text, unsafe_allow_html=True)

    if window == '***CONSECUENCIAS***':
        # st.subheader("La basura espacial se ha multiplicado por 5 en los últimos 10 años")
        st.markdown(
            f"""
            <div style="text-align:center; color:orange; font-size:38px; padding:10px;">
            La basura espacial se ha multiplicado por 5 en los últimos 10 años
            </div>""", unsafe_allow_html=True)
        fig = B1_03()
        PositionImage(fig)
        st.markdown(
            f"""
        <div style="text-align:center; colot:white; font-size:24px; padding:10px;">
            La desmesuradas velocidades de la basura espacial pone en peligro el funcionamiento de los satélites activos e incluso las misiones tripuladas
        </div>
        """,
            unsafe_allow_html=True)
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
