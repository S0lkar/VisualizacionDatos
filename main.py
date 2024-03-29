import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(page_title="Active Satellites in Orbit Around Earth (2016)", page_icon="🌎",
                   initial_sidebar_state="auto")

show_pages(
    [
        Page("intro.py", "Sobre este trabajo", "🚀"),
        Page("bloque01.py", "Introducción al problema", "🚀"),
        Page("bloque02.py", "¿A quién pertenecen?", "🚀"),
        Page("bloque03.py", "¿Qué propósito tienen?", "🚀"),
        Page("bloque04.py", "¿Qué órbitas siguen?", "🚀"),
        Page("bloque05.py", "¿Dónde se fabricaron?", "🚀"),
        Page("bloque06.py", "¿Cómo se puede abordar el problema?", "🚀"),
    ]
)
