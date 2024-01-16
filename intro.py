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
    objetivo_text = """En los últimos años se ha detectado un grave problema en el ámbito espacial relacionado con los satélites y la basura espacial, que quizás esté pasando
    desapercibido para la mayoría de la población.
    Esta es la razón de que nuestro principal objetivo sea exponer información sobre los satélites activos actualmente para evidenciar el grave peligro y las grandes catástrofes que
    que la colisión de un satélite con basura espacial puede ocasionar.
    Para lograrlo, haremos un recorrido histórico por los satélites que siguían activos en el 2016, así como a quién pertenecen, quién los fabricó o en qué órbitas se encuentran.
    """
    st.write(objetivo_text)
    st.subheader("| Conjunto de datos")
    datos_text = """En este trabajo hemos utilizado este <a 
       href="https://www.kaggle.com/datasets/ucsusa/active-satellites/data"> conjunto de datos</a>."""
    st.write(datos_text, unsafe_allow_html=True)
    st.subheader("| Github")
    st.write(
        'Todo nuestro proyecto se encuentra en <a '
        'href="https://github.com/S0lkar/VisualizacionDatos"> nuestro repositorio en GitHub</a>.',
        unsafe_allow_html=True)


B0_Frontend()
