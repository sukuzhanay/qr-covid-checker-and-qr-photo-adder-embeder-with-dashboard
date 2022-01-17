import pandas as pd
import pyrebase as pb
import streamlit as st
import datetime as dt
from datetime import date
from datetime import timedelta
import plotly.graph_objects as plot


# Funcion que calcula el rango de dias entre una fecha y otra
def date_range(start, end):
    delta = end - start
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return delta.days


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




identificador = (input("Introduzca el id: "))

all_users = dd_bb.child("users").get()
# Se obtiene la fecha de vacunacion del usuario
ult_vacuna = dd_bb.child("users/" + identificador + "/fecha_vacunacion").get()





x = []
# Se realiza un split de la fecha recuperada de la base de datos
x = str(ult_vacuna.val()).split("-")
# Se guarda en un array
anio_vacuna = int(x[0])
mes_vacuna = int(x[1])
dia_vacuna = int(x[2])

# Se pasa a tipo Date
tiempo_ult_vacuna = dt.date(anio_vacuna, mes_vacuna, dia_vacuna)
# Se obtiene la fecha actual
tiempo_actual = date.today()
anio = tiempo_actual.year
mes = tiempo_actual.month
dia = tiempo_actual.day
# Se guardan los dias entre las dos fechas
dias_pasado = date_range(tiempo_ult_vacuna, tiempo_actual)

meses_pasados = int(dias_pasado / 30)
anios = int(meses_pasados / 12)
print("Tiempo medio desde la ultima vacunacion: " + str(meses_pasados))

if dias_pasado <= 30:
    if dias_pasado == 1:
        df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [str(dias_pasado) + " día"]})

    else:
        df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [str(dias_pasado) + " días"]})

else:
    if meses_pasados <= 12:
        if meses_pasados == 1:
            df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [str(meses_pasados) + " mes"]})

        else:
            df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [str(meses_pasados) + " meses"]})

    else:
        if anios == 1:
            _meses_pasados = meses_pasados-12
            if _meses_pasados == 1:
                df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [str(anios) + " año " + str(meses_pasados-12) + "mes"]})

            else:
                df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [str(anios) + " año " + str(meses_pasados-12) + "meses"]})

        else:
            _meses_pasados = meses_pasados - 12
            if _meses_pasados == 1:
                df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [str(anios) + " años "+ str(meses_pasados-12) + "mes"]})

            else:
                df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [str(anios) + " años " + str(meses_pasados - 12) + "meses"]})


st.table(df)

