import pyrebase as pb
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ¡¡¡API DE PRUEBA - base de datos falsa!!!
firebaseConfig = {
    "apiKey": "AIzaSyBsyBZDG0BF6F9BAi95G_bW_wVP3xt7_sc",
    "authDomain": "pcd-prueba.firebaseapp.com",
    "databaseURL": "https://pcd-prueba-default-rtdb.europe-west1.firebasedatabase.app/",
    "projectId": "pcd-prueba",
    "storageBucket": "pcd-prueba.appspot.com",
    "messagingSenderId": "547368512451",
    "appId": "1:547368512451:web:e7e22f6f578c608651ab76"
}

firebase = pb.initialize_app(firebaseConfig)
sign_in_up = firebase.auth()
# Login de prueba
mail = "mtrgomez00@gmail.com"
passw = "RandomPass123"
user = sign_in_up.sign_in_with_email_and_password(mail, passw)
db = firebase.database()

all_users = db.child("users").get()

spikevax = 0
comirnaty = 0
covishield = 0
janssen = 0

print(all_users.val)

# Contador de tipo de vacuna
for users in all_users.each():
    if "Spikevax" in str(users.val()):
        spikevax += 1
    elif "Comirnaty" in str(users.val()):
        comirnaty += 1
    elif "Covishield" in str(users.val()):
        covishield += 1
    else:
        janssen += 1

print("Spikevax " + str(spikevax) + "Comirnaty " + str(comirnaty) + "Covishield " + str(covishield) + "Janssen " + str(janssen))

vacunas = ["Spikevax", "Comirnaty", "Covishield", "Janssen"]
valores = [spikevax, comirnaty, covishield, janssen]

# Se crea la grafica
fig = go.Figure(
    go.Pie(
        labels=vacunas,
        values=valores,
        hoverinfo="label+percent",
        textinfo="value"
    ))

# Grafica se pasa a Streamlit
st.header("Vacunas")
st.plotly_chart(fig)
