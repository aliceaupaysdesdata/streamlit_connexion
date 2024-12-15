import streamlit as st
import pandas as pd
import streamlit_option_menu as som
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# ---- USER AUTHENTICATION ----
with open('config_hashed.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialisation de l'authentificateur
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    auto_hash=False
)

# Gestion de la connexion
try:
    authenticator.login(location='sidebar')
except Exception as e:
    st.error(e)


if st.session_state['authentication_status']:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')


    # Menu de navigation
    selection = som.option_menu(
        menu_title=None,
        options=["Accueil", "Photos"]
    )
    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Un chat")
            st.image("https://static.streamlit.io/examples/cat.jpg")
        with col2:
            st.header("Un chien")
            st.image("https://static.streamlit.io/examples/dog.jpg")
        with col3:
            st.header("Un hibou")
            st.image("https://static.streamlit.io/examples/owl.jpg")


elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')

elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')