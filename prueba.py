import pandas as pd
import pyrebase as pb
import streamlit as st
import datetime as dt
from datetime import date
from datetime import timedelta
import altair as alt
import plotly.graph_objects as px
from tkinter import filedialog
from tkinter import *

from numpy import imag
from pygments.lexers import python
import crearQr
import main
import os
import camara2
from hc1_decode import BBDD
from PIL import Image
import requests


root = Tk()

# Datos de Firebase
firebaseConfig = {
    'apiKey': "AIzaSyArmVriibDlBkIJ_3yURB1e3QprmU1z3hY",
    'authDomain': "proyectofinalpcd-816d5.firebaseapp.com/",
    'projectId': "proyectofinalpcd-816d5",
    'databaseURL': "https://proyectofinalpcd-816d5-default-rtdb.europe-west1.firebasedatabase.app",
    'storageBucket': "proyectofinalpcd-816d5.appspot.com",
    'messagingSenderId': "341285184166",
    'appId': "1:341285184166:web:988dd980f771f7b150ca67",
    'measurementId': "G-6DE3ERD9GD"
}

# Iniciamos Firebase y autenticamos
firebase = pb.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()
st.sidebar.title("QRCovid")
c = st.sidebar.container()

# Menu desplegable
menu = st.sidebar.selectbox('Entrar/Registrar', ['Entrar', 'Registrar'])

# Pedimos usuario y contraseña
email = st.sidebar.text_input('Introduce su email')
password = st.sidebar.text_input('Introduce su contraseña', type='password')

c.empty()

# Registrar
if menu == 'Registrar':
    username_ = st.sidebar.text_input(
        'Introduce tu nombre ')
    lastname_ = st.sidebar.text_input(
        'Introduce tu apellido')
    crear_cuenta_button = st.sidebar.button('Crear cuenta')

    if crear_cuenta_button:
        if len(password) < 6:
            st.info('La contraseña debe incluir mas de 6 caracteres')
        else:
            try:
                # Creamos al usuario
                user = auth.create_user_with_email_and_password(email, password)
                st.success('Cuenta creada!')
                st.balloons()  # Decoracion

                # Verificamos al usuario y añadimos datos en la db
                user = auth.sign_in_with_email_and_password(email, password)

                st.title('Bienvenid@ ' + username_)
            except:
                st.error("Error al registrar la cuenta")

# Login
if menu == 'Entrar':

    if email != "":
        if password != "":
            try:
                user_check = auth.sign_in_with_email_and_password(email, password)
                with c:
                    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                    opciones = st.radio('Ir a', ['Home', 'Ajustes'], key="1")

                if opciones == 'Home':
                    c = st.container()
                    with c:
                        main.pauta_media()
                        main.porcentaje_tipo_vacuna()
                        main.porcentaje_pauta_completa()

                    col2, col3 = st.columns(2)
                    with col2:
                        main.tiempo_medio()
                    with col3:
                        main.periodo_vacunacion()
                        main.vacunados_mes()

                if opciones == "Ajustes":
                    qr = st.selectbox("Eliga la acción que desee", ("Crear Qr", "2"))

                    if qr == "Crear Qr":
                        colQr1, colQr2 = st.columns(2)
                        with colQr1:
                            scan = st.button("Scan")
                        with colQr2:
                            tomarFoto = st.button("Tomar foto")

                        if scan:
                            try:
                                # Pedir Qr
                                Qr_path = filedialog.askopenfilename(master=root)
                                Leido_Qr = crearQr.pedirQrGuardado(Qr_path)
                                # Pedir foto
                                path_Foto = filedialog.askopenfilename(master=root)
                                # crear Qr
                                crearQr.make_qrcode(data=Leido_Qr, save_path='./QRCovid.png', icon_path=path_Foto)
                                storage.child("QrsEmbebidos/" + email + "/QrEmbebido.png").put("QRCovid.png")
                                st.success("Guardado correctamente")

                                base = BBDD().decode(Leido_Qr)


                            except:
                                st.error("Error")

                        if tomarFoto:
                            hc1 = crearQr.pedirQrCamara()
                            camara2.hacerFotoCara()
                            crearQr.make_qrcode(data=hc1, save_path='./QRCovid.png', icon_path='./fotoCara.png')
                            storage.child("QrsEmbebidos/" + email + "/QrEmbebido.png").put("QRCovid.png")
                            st.success("Guardado correctamente")

                        try:
                            imageUrl = storage.child('QrsEmbebidos/'+email+'/QrEmbebido.png').get_url(user_check['idToken'])
                            im = Image.open(requests.get(imageUrl, stream=True).raw)
                            st.write("Qr embebido:")
                            st.image(imageUrl)
                        except:
                            st.error("No HA Embebido su QR")


                    if qr == "2":
                        st.info("eleccion 2")




            except:
                st.error('Gmail o Contraseña incorrectos')
