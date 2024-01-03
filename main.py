# ------- Módulos para traer las gráficas a streamlit -------
import streamlit as st
# import bloque01 as B1
import bloque02 as B2
# import bloque03 as B3
import bloque04 as B4


# import bloque05 as B5
# import bloque06 as B6


# ------- Contenido general de la página -------
# Aquí se dan las instrucciones para montar la página (definiendo el estilo, gráficas...) principal.
# Tal y como está montado, podríamos tener diferentes estilos por apartados

@st.cache_resource
def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(page_title="Active Satellites in Orbit Around Earth till 2016", page_icon="🌎",
                   initial_sidebar_state="collapsed")


def add_audio(filename):
    audio_file = open(filename, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mpeg")


local_css("frontend.css")
tab = st.tabs(["Presentación", "Introducción al problema", "¿Cómo hemos llegado aquí",
               "¿A quién pertenecen y qué propósito tienen?", "¿Qué órbitas siguen?",
               "¿Dónde se fabricaron?", "¿Cómo se puede abordar el problema"])

# ----------------- Introducción -----------------
with tab[0]:
    add_audio("audio/intro.mp3")
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
        intro_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla fringilla ligula eu purus 
        egestas, non elementum sem dignissim. Vivamus tristique porta molestie. Nam semper elementum ante sed 
        interdum. Quisque a augue quis lectus placerat commodo et vitae massa. Donec ipsum leo, ultrices non aliquam 
        quis, ultricies in erat. Pellentesque sed pharetra dui. Aenean sed accumsan velit, ut elementum sem."""
        # Este color resalta algo más que el grisáceo y sigue en la paleta
        st.write(f'<p style="color:#f4ebd0">{intro_text}</p>', unsafe_allow_html=True)
    # ---------------------------------------------------------------------------------

    st.subheader("| Objetivo del trabajo")
    st.write(
        # Color normal de texto con ejemplos de cómo usar texto en negrita y en cursiva
        '<p style="color:#9c9d9f"> Lorem <b>ipsum</b> <i>dolor</i> sit amet. </p>',
        unsafe_allow_html=True,
    )
    st.subheader("| Conjunto de datos")

    st.subheader("| Github")
    st.write(
        '<p style="color:#9c9d9f">Toda nuestra historia se encuentra en <a '
        'href="https://github.com/S0lkar/VisualizacionDatos">nuestro repositorio en GitHub</a>.</p><br>',
        unsafe_allow_html=True,
    )

# Código del Bloque 1
# with tab[1]:
#    B1.B1_Frontend()

# Código del Bloque 2
with tab[2]:
    B2.B2_Frontend()

# Código del Bloque 3
# with tab[3]:
#    B3.B3_Frontend()

# Código del Bloque 4
with tab[4]:
    B4.B4_Frontend()

# Código del Bloque 5
# with tab[5]:
#    B5.B5_Frontend()

# Código del Bloque 6
# with tab[6]:
#    B6.B6_Frontend()
