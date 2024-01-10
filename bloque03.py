from CommonTools import *
# add to nav
add_page_title(initial_sidebar_state="expanded", layout="wide")
local_css("frontend.css")

def B3_01():
    B3_0X = pd.read_csv(FILENAME)
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
    return fig


def B3_Frontend():
    audio_file = open("audio/intro.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mpeg")
    
    st.subheader("| Título")
    st.write("""
             Lorem ipsum noseque nosecuantos.
             """)
    PositionImage(B3_01())
    
    
    
B3_Frontend()