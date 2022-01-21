import pandas as pd
import pyrebase as pb
import streamlit as st
import datetime as dt
from datetime import date
from datetime import timedelta
import altair as alt


# Funcion que calcula el rango de dias entre una fecha y otra
def date_range(start, end):
    delta = end - start
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return delta.days


# Base de datos
firebaseConfig = {
  "apiKey": "AIzaSyArmVriibDlBkIJ_3yURB1e3QprmU1z3hY",
  "authDomain": "proyectofinalpcd-816d5.firebaseapp.com",
  "databaseURL": "https://proyectofinalpcd-816d5-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "proyectofinalpcd-816d5",
  "storageBucket": "proyectofinalpcd-816d5.appspot.com",
  "messagingSenderId": "341285184166",
  "appId": "1:341285184166:web:988dd980f771f7b150ca67",
  "measurementId": "G-6DE3ERD9GD"
};

firebase = pb.initialize_app(firebaseConfig)
sign_in_up = firebase.auth()
dd_bb = firebase.database()
# Login
mail = "lembajosa@gmail.com"
password = "patata123"
user = sign_in_up.sign_in_with_email_and_password(mail, password)

#Se aniaden otro usuarios para realizar las pruebas

dd_bb.child("Usuarios/MtxK7EJ7D3xFVkCIZXe/Nombre").set("Prueba")
dd_bb.child("Usuarios/MtxK7EJ7D3xFVkCIZXe/Datos_de_vacunacion/Fecha_de_Vacunación").set("2021-11-14")

dd_bb.child("Usuarios/HfjgYt6Fvdu5kPj4vg3/Nombre").set("Prueba2")
dd_bb.child("Usuarios/HfjgYt6Fvdu5kPj4vg3/Datos_de_vacunacion/Fecha_de_Vacunación").set("2020-08-22")

dd_bb.child("Usuarios/Kghru6idFeSai9KIf3q/Nombre").set("Prueba3")
dd_bb.child("Usuarios/Kghru6idFeSai9KIf3q/Datos_de_vacunacion/Fecha_de_Vacunación").set("2021-11-23")


# Se obtienen todos los usuarios
all_users = dd_bb.child("Usuarios").get()
# Fecha actual
tiempo_actual = date.today()

x = []
y = []

# Variables donde se guardaran los resultados
UnoMeses = 0
TresMeses = 0
SeisMeses = 0
NueveMeses = 0
DoceMeses = 0
QuinceMeses = 0


contador = 0;
# Se recorre todos los usuarios en busca de la fecha de vacunancion
for users in all_users.each():
    if 'Fecha_de_Vacunación' in str(users.val()):
        ult_vacuna = dd_bb.child("Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/Fecha_de_Vacunación").get()
        # Las fechas se guardan en un array
        x.append(ult_vacuna.val())
        # Se guarda en y la fecha dividida con el split
        y = str(x[contador]).split("-")

        # Se guardan en arrays
        anio_vacuna = int(y[0])
        mes_vacuna = int(y[1])
        dia_vacuna = int(y[2])

        # Se crea la fecha con los datos guardados
        tiempo_ult_vacuna = dt.date(anio_vacuna, mes_vacuna, dia_vacuna)

        # Se obtienen las diferentes partes de la fecha actual
        anio = tiempo_actual.year
        mes = tiempo_actual.month
        dia = tiempo_actual.day

        # Se guardan los dias entre las dos fechas
        dias_pasado = date_range(tiempo_ult_vacuna, tiempo_actual)
        meses_pasados = int(dias_pasado / 30)
        anios = int(meses_pasados / 12)

        # Se realizan las comprobaciones necesarias
        if dias_pasado < 30:
            print(dias_pasado)
        elif 1 <= meses_pasados <=2:
            UnoMeses +=1
        elif 3 <= meses_pasados <= 5:
            TresMeses +=1
        elif 6 <= meses_pasados <= 8:
            SeisMeses +=1
        elif 9 <= meses_pasados <= 11:
            NueveMeses +=1
        elif 12 <= meses_pasados <= 14:
            DoceMeses +=1
        elif meses_pasados >= 15:
            QuinceMeses +=1

        # Una vez terminada de sumar 1, en el mes correspondiente, se suma el contador y realiza lo mismo con los siguientes usaurios
        contador+=1


# Se cargan los valores del grafico
source = pd.DataFrame({
    'Tiempo transcurrido': ["1 meses", "3 meses", "6 meses", "9 meses", "12 meses", "15 meses"],
    'Número de personas': [UnoMeses, TresMeses, SeisMeses, NueveMeses, DoceMeses, QuinceMeses]
})

chart = alt.Chart(source).mark_bar(color='purple').encode(
    x=alt.X("Tiempo transcurrido:O", title="Tiempo Transcurrido", sort=["1 meses", "3 meses", "6 meses", "9 meses", "12 meses", "15 meses"]),
    y=alt.Y("Número de personas:Q", title="Número de personas", axis=alt.Axis(tickMinStep=1), scale=alt.Scale(domain=(0, contador+1))),
)

st.altair_chart(chart)
