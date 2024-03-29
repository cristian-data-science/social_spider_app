import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import time
import plotly.express as px
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder


def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
        text = link.split('=')[0]
        return f'<a target="_blank" href="{link}">{link}</a>'
st.set_page_config(page_title="Social Spider App",layout="wide")
col1 = st.sidebar

col2, col3 = st.columns((3,1))



col2.title("Social Spider App")
col2.markdown("""
 Esta app contrata a unos bots hechos en python para revisar constantemente las tendencias de Chile en las principales redes sociales del momento
""")




# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home",'Tendencias de Google', 'Tendencias de Twitter' , 'Tendencias de Tiktok', 'Tendencias de Youtube'], 
        icons=['house', 'google', 'twitter', 'tiktok', 'youtube'], menu_icon="cast", default_index=0)


    if selected == "Tendencias de Google":
        st.sidebar.markdown("<div><img src='http://2.bp.blogspot.com/-LfB9P5GRyIY/VjETrBoHwHI/AAAAAAAAH4Q/5naYJfDbPqM/s1600/google_buscador.png' width=130 /><h1 style='display:inline-block'>Google</h1></div>", unsafe_allow_html=True)
        st.sidebar.markdown("Este dashboard muestra las ultimas busquedas de Google en Chile")

    if selected == "Tendencias de Twitter":
        st.sidebar.markdown("<div><img src='https://abylightstudios.es/wp-content/uploads/2021/08/icono-twitter-abylight-studios.png' width=125 /><h1 style='display:inline-block'>Twitter</h1></div>", unsafe_allow_html=True)
        st.sidebar.markdown("Este dashboard muestra los ultimos #Hashtags de Twitter en Chile") 

    if selected == "Tendencias de Tiktok":
        st.sidebar.markdown("<div><img src='https://png2png.com/wp-content/uploads/2021/08/Tiktok-logo-png.png' width=135/><h1 style='display:inline-block'>Tiktok</h1></div>", unsafe_allow_html=True)
        st.sidebar.markdown("Este dashboard muestra las ultimas tendencias de Tiktok en Chile") 

    if selected == "Tendencias de Youtube":
        st.sidebar.markdown("<div><img src='https://images.vexels.com/media/users/3/137425/isolated/lists/f2ea1ded4d037633f687ee389a571086-logotipo-de-icono-de-youtube.png' width=135 /><h1 style='display:inline-block'>Youtube</h1></div>", unsafe_allow_html=True)
        st.sidebar.markdown("Este dashboard muestra las ultimas tendencias de Youtube en Chile")     


if selected == "Tendencias de Google":
    #st.markdown("### Top búsquedas hechas en el principal buscador: ")
        # graficando con barras
    google_bar = pd.read_csv("./resultados/google.csv", index_col="top")
    
    google_bar["rand"] = (np.random.uniform(1, 1.2,len(google_bar['busqueda'])))
    google_bar["rand"] = google_bar["rand"] * google_bar['busqueda']
    google_bar["rand"] = google_bar["rand"].astype(int)
    google_bar['busqueda'] = google_bar['rand']
    google_bar = google_bar[["trend", "busqueda", "link"]]
    fig = px.bar(google_bar, x='trend', y='busqueda', color='busqueda', color_continuous_scale='icefire')
    fig.update_layout(
        title='Cantidad de busquedas en las ultimas 48 horas', 
        xaxis = dict(
            showgrid=True

        ), 
        yaxis = dict(
            title='busqueda organica', 
            showgrid=True
        ), 
        legend = dict(
            orientation='v'
        ), 
        barmode='group' 
        #paper_bgcolor='#F00000'
    )
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

    col2.plotly_chart(fig, use_container_width=True)

   
    
    
    google = pd.read_csv("./resultados/google.csv", index_col="top")
    # link is the column with hyperlinks
    google['link'] = google['link'].apply(make_clickable)
    google = google.to_html(escape=False)
    #col2.write(google, unsafe_allow_html=True)
    
    
    g2 = GridOptionsBuilder.from_dataframe(google_bar)
    #g2.configure_pagination()
    g2.configure_side_bar()
    #g2.configure_default_column(editable=False)
    gridOptions = g2.build()

    top_tab = google_bar.sort_values("busqueda", ascending=False).head(1)
    top_busqueda = top_tab['busqueda'].max()
    top_trend = top_tab['trend'].max()

    print(top_busqueda)

    with col2:
        col2.info('**La tendencia mayor buscada es:   '+ '"'+ top_trend.upper()+ '"'+ ' con '+  str(top_busqueda) + ' ' + 'de busquedas.')
        AgGrid(google_bar, gridOptions=gridOptions,theme='streamlit',fit_columns_on_grid_load=True, enable_enterprise_modules=True)#, height=892)









hide_st_style = """
            <style>
            footer {visibility: hidden;}
;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
