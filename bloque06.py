from CommonTools import *
def PositionImage2(data, proportions = [0.15, 0.7, 0.15], usecol = 1):
    cols = st.columns(proportions)
    with cols[usecol]:
        st.image(data)
    pass
# add to nav
add_page_title(initial_sidebar_state="expanded", layout="wide")
local_css("frontend.css")

st.subheader("| Una propuesta desde Andalucía")
st.write("Propuesta de Sevilla y San Fernando para reducir la basura espacial y asi ayudar a conservar los satelites mas cercanos a la tierra, ya que están mas expuestos a choques.")
st.write("Debido al problema real existente de la basura espacial, la Armada española, con su Real Observatorio de San Fernando (Cádiz), participa en la detección de esos objetos, enviando los datos al centro Español de Vigilancia y Seguimiento Espacial para calcular las órbitas de los mismos, con el fin de prever si un nuevo objeto va a reentrar en la atmósfera o si va a colisionar con otro objeto, aumentando así la basura espacial. Cuenta ya con dos intrumentos para este estudio: un telescopio, y una estación de telemetría laser")
PositionImage2('./imgs/conclusion_espana.jpg')
 

st.subheader("| Iniciativa E.T.PACK ")
st.write("La iniciativa E.T.PACK  se trata de un proyecto coordinado por insituciones europeas, entre ellas la Universidad Carlos III de Madrid y la empresa española SENER.\n Su objetivo es proporcionar un dispositivo autónomo de desorbitado que podrá ser montado en los satélites del futuro y permitirá eliminarlos al final de su vida útil en lugar de dejarlos en órbita.")
PositionImage2('./imgs/iniciativa.PNG')
st.subheader("| Bibliografía")
datos_text = """En este trabajo hemos utilizado este <a 
       href="https://www.kaggle.com/datasets/ucsusa/active-satellites/data">conjunto de datos</a>."""

st.markdown(datos_text, unsafe_allow_html=True)
url = "https://www.elespanol.com/espana/20180401/protege-armada-basura-espacial/295721195_0.html"

enlace = f'<a href="{url}">Así nos protege la Armada de la basura espacial</a>.'

st.write(enlace, unsafe_allow_html=True)

url2 = "https://spanish-presidency.consilium.europa.eu/eu/albisteak/europa-pionera-retirada-restos-satelites-mejorar-trafico-espacial/"

enlace2 = f'<a href="{url}">Así nos protege la Armada de la basura espacial</a>.'

st.write(enlace2, unsafe_allow_html=True)
