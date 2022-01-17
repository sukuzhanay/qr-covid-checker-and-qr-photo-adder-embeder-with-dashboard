import pandas
import numpy as np
import pyrebase as pb
import streamlit as st
import datetime as dt
from datetime import date
from datetime import timedelta

# Base de datos de PRUEBA
firebaseConfig = {
    "apiKey": "AIzaSyBsyBZDG0BF6F9BAi95G_bW_wVP3xt7_sc",
    "authDomain": "pcd-prueba.firebaseapp.com",
    "databaseURL": "https://pcd-prueba-default-rtdb.europe-west1.firebasedatabase.app/",
    "projectId": "pcd-prueba",
    "storageBucket": "pcd-prueba.appspot.com",
    "messagingSenderId": "547368512451",
    "appId": "1:547368512451:web:e7e22f6f578c608651ab76"
};

firebase = pb.initialize_app(firebaseConfig)
sign_in_up = firebase.auth()
dd_bb = firebase.database()
# Login de prueba
mail = "lembajosa@gmail.com"
password = "patata123"
user = sign_in_up.sign_in_with_email_and_password(mail, password)

# Se obtienen todos los usuarios
all_users = dd_bb.child("users").get()
# Fecha actual
tiempo_actual = date.today()

x = []
# Se recorre todos los usuarios en busca de la fecha de vacunancion
for users in all_users.each():
    if 'fecha_vacunacion' in str(users.val()):
        ult_vacuna = dd_bb.child("users/" + str(users.key()) + "/fecha_vacunacion").get()
        # Se imprime la fecha
        print(ult_vacuna.key() + ': ' + ult_vacuna.val())
        # Las fechas se guardan en un array
        x.append(ult_vacuna.val())

# Las vacunas se guardan como strings

y = []
# Las fechas se guardan en otro array como elementos unicos

for i in x:
    separado = i.split("\n")
    y.append(separado)



