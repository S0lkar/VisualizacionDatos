from CommonTools import *
# add to nav
add_page_title(initial_sidebar_state="expanded", layout="wide")
local_css("frontend.css")

def B5_Frontend():

    # Inicialización de st.session_state (para pantalla completa)
    if "use_container_width" not in st.session_state:
        st.session_state["use_container_width"] = True

    data = pd.read_csv("database.csv")
    #names = data.columns.tolist()
    # print(names)
    country_contractor = data["Country of Contractor"] # tiene 1419

    # --- para los años y añadirlo en la table
    data["Date of Launch"] = pd.to_datetime(data["Date of Launch"])  # Convertir la columna a tipo datetime si aún no está en ese formato

    # Obtener el año de la columna 'Date of Launch'
    data["Year of Launch"] = data["Date of Launch"].dt.year  # Crear una nueva columna con el año de lanzamiento

    # -----

    st.write(""" Hemos registrado la existencia de 158 vehículos de lanzamiento, cada uno con sus propias características y 
            contribución al avance de la exploración espacial. Pero, ¿cuáles son los más populares?🚀🚀""")

    st.write("Aquí presentamos una selección de los vehículos más lanzados:")
    # data1 = pd.DataFrame(data["Launch Vehicle"].value_counts().head(15))
    # st.dataframe(data1,use_container_width=st.session_state.use_container_width)

    conteo = (data["Launch Vehicle"].value_counts().head(15))
    # -----
    # Crear un gráfico de barras horizontal con Plotly Express
    fig = px.bar(conteo, orientation='h', text = conteo.values, labels={'value': 'Cantidad', 'index': 'Launch Vehicle'},
                title='Recuento de vehículos de lanzamiento (Top 15)')
    fig.update_traces(marker_color='darkred')
    fig.update_layout(xaxis_title='', yaxis_title='', showlegend=False, title_x=0.2,title_font_size=24)

    # Mostrar el gráfico usando Streamlit
    #st.plotly_chart(fig)
    PositionImage(fig)
    # ----- FIN

    # Diccionario de videos por vehículo (con enlaces de YouTube)
    videos = {
        'Atlas 5': 'https://www.youtube.com/watch?v=2kLH15-6jWk',
        'Dnepr': 'https://www.youtube.com/watch?v=laOS59AysG0',
        'Proton M': 'https://www.youtube.com/watch?v=12frRUrHebI',
        'Ariane 5 ECA': 'https://www.youtube.com/watch?v=V8LQ_iotrEA',
        'Delta 2': 'https://www.youtube.com/watch?v=OJSwI4Dverc',
        'Ariane 5': 'https://www.youtube.com/watch?v=UaYZieeCX68',
        'Rokot': 'https://www.youtube.com/watch?v=uY8Ns5pT0vQ',
        'Delta 2 7920': 'https://www.youtube.com/watch?v=UMfTthzfByE',
        'Proton K': 'https://www.youtube.com/watch?v=k8PZuiSY2UA',
        'Falcon 9': 'https://www.youtube.com/watch?v=Z4TXCZG_NEY',
        'Long March 3B': 'https://www.youtube.com/watch?v=_7F0s6AcFdg',
        'Long March 2C': 'https://www.youtube.com/watch?v=PmlCgkldKX8',
        'Long March 2D': 'https://www.youtube.com/watch?v=TvlvPxsLLX4',
        'Nanorack Deployer': 'https://www.youtube.com/watch?v=gRMgBUQxsms',
        'Long March 4C': 'https://www.youtube.com/watch?v=zC4kv-rlmyE'
    }

    # Parte de simulacion de lanzamiento espacial 
    st.title('Simulador de Lanzamiento Espacial')
    st.write('''Desde los cohetes más icónicos hasta las imponentes naves espaciales, ¡tienes el poder de elegir! 
            Selecciona tu vehículo de lanzamiento preferido de la lista y prepárate para el despegue🚀🚀''')

    # Selección del vehículo de lanzamiento
    vehiculos_lanzamiento = list(videos.keys())  
    vehiculo_seleccionado = st.selectbox('Seleccione un vehículo de lanzamiento:', vehiculos_lanzamiento)

    # Mostrar video del vehículo seleccionado desde YouTube
    if vehiculo_seleccionado in videos:
        st.video(videos[vehiculo_seleccionado])


    # -----

    st.title("Análisis de sitios de lanzamiento de vehículos espaciales")

    
    data = pd.read_csv("database.csv")
    data['Country of Contractor'] = data['Country of Contractor'].str.replace('France, UK, Germany', 'France/ UK/Germany')
    data['Country of Contractor'] = data['Country of Contractor'].str.replace('International', 'Ecuador')
    data['Country of Contractor'] = data['Country of Contractor'].str.replace('Multinational', 'Ecuador')

    # -----


    # Dividir la columna 'Países' en múltiples columnas usando "/"

    data["Country of Contractor"].dropna(inplace=True)

    df_separated = data["Country of Contractor"].str.split('/', expand=True)

    # Seleccionar el primer país de cada fila
    data['First_country'] = df_separated[0]
    data['First_country'] = data['First_country'].str.strip()

    # Seleccionar el primer país de cada fila
    data['First_country'] = df_separated[0]

    # -----

    # Obtener la cantidad de sitios de lanzamiento por país
    conteo_paises =data['First_country'].value_counts().sort_values(ascending=False)

    # Crear un gráfico de barras con PLOTLY EXPRESS
    fig = px.bar(x=conteo_paises.index, y=conteo_paises.values, labels={'x': 'País', 'y': 'Cantidad'},
             title='Recuento de países de fabricación de vehículos')
    fig.update_traces(marker_color='darkred')  
    fig.update_layout(title_x=0.2,title_font_size=24)

    PositionImage(fig)
    # ----
    
    st.markdown("""<p style='color:gold;font-size:20px;font-weight:bold;'>Tras ver el recuento de <span style='color:darkred;'>DÓNDE</span> se han fabricado, toca observar <span style='color:darkred;'>HACIA DÓNDE</span> se han destinado para su lanzamiento. ¡¡Veámoslo!!</p>""", unsafe_allow_html=True)

    # Seleccionar un país mediante el gráfico de barras
    selected_country = st.selectbox('Selecciona un país', conteo_paises.index)

    # Diccionario con las coordenadas de los sitios de lanzamiento
    coordenadas_lanzamiento = {
        'Baikonur Cosmodrome': (45.9644, 63.3056),  
        'Cape Canaveral': (28.5721, -80.6480),
        'Dombarovsky Air Base': (51.0614, 59.8542),
        'Guiana Space Center': (5.2360, -52.7681),
        'International Space Station': (51.6417, -0.1499),
        'Jiuquan Satellite Launch Center': (40.9583, 100.2917),
        'Kodiak Launch Complex': (57.4708, -152.2951),
        'Kwajalein Island': (8.7209, 167.736),
        'Naro Space Center': (34.6366, 127.0973),
        'Palmachim Launch Complex': (31.7922, 34.6304),
        'Plesetsk Cosmodrome': (62.9271, 40.5774),
        'Satish Dhawan Space Center': (13.7337, 80.2354),
        'Sea Launch': (0.0, 0.0), 
        'Sea Launch (Odyssey)': (0.0, 0.0), 
        'Svobodny Cosmodrome': (51.4023, 128.2970),
        'Taiyuan Launch Center': (38.8428, 111.6184),
        'Tanegashima Space Center': (30.3607, 130.9587),
        'Uchinoura Space Center': (31.2519, 131.0806),
        'Vandenberg AFB': (34.7420, -120.5724),
        'Vostochny Cosmodrome': (51.8845, 128.3331),
        'Wallops Island Flight Facility': (37.9404, -75.4665),
        'Xichang Satellite Launch Center': (28.2463, 102.0268)
    }


    # Diccionario que asocia las ubicaciones de lanzamiento con sus imágenes
    imagenes_lanzamiento = { 
        'Baikonur Cosmodrome': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Soyuz_expedition_19_launch_pad.jpg/250px-Soyuz_expedition_19_launch_pad.jpg',  # Reemplazar con las coordenadas reales
        'Cape Canaveral': 'https://upload.wikimedia.org/wikipedia/commons/9/92/Atlas_V_551_at_Launch_Pad_41.jpg',
        'Dombarovsky Air Base': 'https://destination-orbite.net/astronautique/centres-spatiaux/images/full_hr/dombarovsky.jpg',
        'Guiana Space Center': 'https://galileognss.eu/wp-content/uploads/2018/04/CSG-site.jpg',
        'International Space Station': 'https://spaceflightnow.com/wp-content/uploads/2015/11/PREVIEW1.jpg',
        'Jiuquan Satellite Launch Center': 'https://chinaspacereport.files.wordpress.com/2016/05/12947184.jpg',
        'Kodiak Launch Complex': 'https://cloudfront-us-east-1.images.arcpublishing.com/adn/EV5U7N2M6NCEHI6RSBWFWBALL4.webp',
        'Kwajalein Island': 'https://spaceflightnow.com/falcon/003/images/falcon1onpad.jpg',
        'Naro Space Center': 'https://upload.wikimedia.org/wikipedia/commons/b/b0/KSLV-1_Naro_Replica.jpg',
        'Palmachim Launch Complex':'https://parabolicarc.com/wp-content/uploads/2020/05/Falcon9_Crew_Dragon_Demo2_launch.jpg',
        'Plesetsk Cosmodrome': 'https://cdn-media.tass.ru/width/1020_b9261fa1/tass/m2/en/uploads/i/20211008/1335955.jpg',
        'Satish Dhawan Space Center': 'https://images.news9live.com/wp-content/uploads/2023/07/Satish-Dhawan-Space-Centre.png',
        'Sea Launch': 'https://spacewatch.global/wp-content/uploads/2018/08/Sea_Launch_Image_source_spacenews.jpg',  # Reemplazar con las coordenadas reales
        'Sea Launch (Odyssey)': 'https://upload.wikimedia.org/wikipedia/commons/a/a5/Sea_launch_1.jpg',  # Reemplazar con las coordenadas reales
        'Svobodny Cosmodrome': 'https://cdn.mos.cms.futurecdn.net/fr8xobYC2FA6vFjvya5xyV.jpg',
        'Taiyuan Launch Center': 'https://chinaspacereport.files.wordpress.com/2016/06/122420abbvym91bhhbjhmy-e1464813245798.jpg',
        'Tanegashima Space Center': 'https://asd.gsfc.nasa.gov/blueshift/wp-content/uploads/2015/12/Japan-Aerospace-Exploration-Agency-JAXA-NASA-Mitsubishi-Heavy-Industries-H-IIB-rocket-photo-credit-JAXA-posted-on-SpaceFlight-Insider.jpg',
        'Uchinoura Space Center': 'data:image/jpeg;base64,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',
        'Vandenberg AFB': 'https://upload.wikimedia.org/wikipedia/commons/d/d4/Iridium-1_Mission_%2831450835954%29.jpg',
        'Vostochny Cosmodrome': 'https://upload.wikimedia.org/wikipedia/commons/a/ac/%D0%A1%D1%82%D0%B0%D1%80%D1%82%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81_%D0%BA%D0%BE%D1%81%D0%BC%D0%BE%D0%B4%D1%80%D0%BE%D0%BC%D0%B0_%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9_%D0%BF%D0%B5%D1%80%D0%B5%D0%B4_%D0%BF%D0%B5%D1%80%D0%B2%D1%8B%D0%BC_%D0%BF%D1%83%D1%81%D0%BA%D0%BE%D0%BC.jpg',
        'Wallops Island Flight Facility': 'https://media.defense.gov/2013/Sep/06/2000751479/780/780/0/090613-A-CE999-001.JPG',
        'Xichang Satellite Launch Center': 'https://video.cgtn.com/news/3d3d674d7a6b7a4e31457a6333566d54/video/c8bc07ce4a7343c08793d8f7ed729366/c8bc07ce4a7343c08793d8f7ed729366.jpg'
    }

    if selected_country:
        
        filtered_data = data[data['First_country'] == selected_country]
        launch_sites = filtered_data['Launch Site'].unique()
        
        # Mostrar el mapa interactivo con los sitios de lanzamiento usando Folium
        m = folium.Map(location=[0, 0], zoom_start=2)

        # Agregar marcadores al mapa para los sitios de lanzamiento asociados al país seleccionado
        for site in launch_sites:
            site_name = site #ESTO
            image_url = imagenes_lanzamiento.get(site)
            coordinates = coordenadas_lanzamiento.get(site)
            popup_content = f'<h3>{site_name}</h3>'
            popup_content += f'<img src="{image_url}" alt="{site}" style="max-height:200px;max-width:300px;">'
            
            if coordinates:
                
                folium.Marker(
                    location=coordinates,
                    popup=folium.Popup(popup_content, max_width=400),
                    icon=folium.Icon(color='blue', icon='rocket')
                ).add_to(m)

        # Mostrar el mapa interactivo en Streamlit
        st.markdown(f"### Lugares de lanzamiento en {selected_country}:")
        st.markdown("")
        st.markdown("")
        st.components.v1.html(m._repr_html_(), width=800, height=600)


B5_Frontend()