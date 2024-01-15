import streamlit as st
import time


def countdown_timer(seconds):
   # while seconds:
    #    st.text(f"Tiempo restante: {seconds}")
    #    time.sleep(1)
    #    seconds -= 1

    image_paths = ['./imgs/0.jpg','./imgs/1.jpg', './imgs/2.jpg', './imgs/3.jpg', './imgs/5.jpg']
    container = st.empty()

    for i in range(len(image_paths),0,-1):
        container.image(image_paths[i-1])
        time.sleep(2)
        container.empty()
    
    st.header("DESPEGAMOS!")
    st.write("Reproducción sonido despegue")
    
    


st.title("¡¡BIENVENIDOS A BORDO 🚀🚀!!")

# Configurar el tiempo inicial en segundos
tiempo_inicial = 5
countdown_timer(tiempo_inicial)

