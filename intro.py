from CommonTools import *

# add to nav
add_page_title(initial_sidebar_state="expanded", layout="wide")
local_css("frontend.css")


def B0_Frontend():
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
        intro_text = """¡Bienvenid@ a bordo!\nEste es un trabajo para la asignatura Visualización de datos del Máster
        en Inteligencia Artificial de la Universidad Loyola Andalucía por lo que tiene un objetivo meramente académico"""
        st.write(intro_text)
    # ---------------------------------------------------------------------------------

    st.subheader("| Objetivo del trabajo")
    objetivo_text = """Analizar y exponer la problemática de la basura espacial haciendo un recorrido por un conjunto
       de datos de los satélites activos a fecha de 2016"""
    st.write(objetivo_text)
    st.subheader("| Conjunto de datos")
    datos_text = """En este trabajo hemos utilizado este <a 
       href="https://www.kaggle.com/datasets/ucsusa/active-satellites/data"> conjunto de datos</a>"""
    st.write(datos_text, unsafe_allow_html=True)
    st.subheader("| Github")
    st.write(
        'Toda nuestra historia se encuentra en <a '
        'href="https://github.com/S0lkar/VisualizacionDatos"> nuestro repositorio en GitHub</a>.',
        unsafe_allow_html=True)


B0_Frontend()
