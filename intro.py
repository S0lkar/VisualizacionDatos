from CommonTools import *
import time

# add to nav
add_page_title(initial_sidebar_state="expanded", layout="wide")
local_css("frontend.css")


def Ninonino():
    image_paths = ['./imgs/0.png','./imgs/1.png', './imgs/2.png', './imgs/3.png', './imgs/4.png', './imgs/5.png']
    container = st.empty()
    proportions = [0.15, 0.7, 0.15]
    cols = st.columns(proportions)
    for i in range(len(image_paths),0,-1):
        with cols[1]:
            container.image(image_paths[i-1])
        time.sleep(2)
        container.empty()
    
    containter = st.header("¡DESPEGAMOS!")

def B0_Frontend():
    container = st.video('./imgs/Cuenta regresiva.mp4', format="video/mp4", start_time=0)
    time.sleep(7)
    container.empty()
    #Ninonino()
    st.subheader("| Presentación")
    # Ejemplo de como poner 'imagen | texto' (funciona para imágenes estáticas con 'st.image(ruta)' tambien)
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # Plot de una gráfica
        st.image('./imgs/img_intro.jpg')
        st.caption(
            "Una historia especialmente espacial sobre los satélites del mundo.", unsafe_allow_html=True
        )
    with col2:
        intro_text = """¡Bienvenid@ a bordo!\nEste es un trabajo desarrollado en la asignatura Visualización de datos del Máster
        en Inteligencia Artificial de la Universidad Loyola Andalucía, con un objetivo fundamentalmente académico. ¡Esperamos que le guste!"""
        st.write(intro_text)
    # ---------------------------------------------------------------------------------

    st.subheader("| Objetivo del trabajo")
    objetivo_text = """Durante los últimos años se ha detectado un problema en el ámbito espacial relacionado con los satélites y basura espacial.
    España juega un papel fundamental en la prevención y solución de esta situación. Sin embargo, es una historia poco conocida hoy en día.
    Nuestro objetivo principal es exponer información sobre los satélites actuales para demostrar que pueden surgir grandes pérdidas
    globales si empiezan a suceder colisiones de satélites activos con la basura espacial, además de fomentar el plan europeo de prevención.
    Para lograrlo, haremos un recorrido histórico de la situación desde los primeros satélites hasta los lanzamientos más recientes (hasta 2016),
    expondremos información sobre qué países se verían más afectados (fabricantes y propietarios) y en qué órbitas son más comúnes encontrar los
    satélites activos.
    """
    st.write(objetivo_text)
    st.subheader("| Github")
    st.write(
        'Todo nuestro proyecto se encuentra en <a '
        'href="https://github.com/S0lkar/VisualizacionDatos"> nuestro repositorio en GitHub</a>.',
        unsafe_allow_html=True)


B0_Frontend()
