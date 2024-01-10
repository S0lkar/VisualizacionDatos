import streamlit as st
from st_pages import add_page_title

# add to nav
add_page_title()


def add_audio(filename):
    audio_file = open(filename, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mpeg")


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
        intro_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla fringilla ligula eu purus
            egestas, non elementum sem dignissim. Vivamus tristique porta molestie. Nam semper elementum ante sed
            interdum. Quisque a augue quis lectus placerat commodo et vitae massa. Donec ipsum leo, ultrices non aliquam
            quis, ultricies in erat. Pellentesque sed pharetra dui. Aenean sed accumsan velit, ut elementum sem."""
        # Este color resalta algo más que el grisáceo y sigue en la paleta
        st.write(intro_text, unsafe_allow_html=True)
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
        'Toda nuestra historia se encuentra en <a '
        'href="https://github.com/S0lkar/VisualizacionDatos">nuestro repositorio en GitHub</a>.</p><br>',
        unsafe_allow_html=True,
    )

B0_Frontend()
