import pyrebase as pb
import streamlit as st
import pandas as pd

firebaseConfig = {
  "apiKey": "AIzaSyArmVriibDlBkIJ_3yURB1e3QprmU1z3hY",
  "authDomain": "proyectofinalpcd-816d5.firebaseapp.com",
  "databaseURL": "https://proyectofinalpcd-816d5-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "proyectofinalpcd-816d5",
  "storageBucket": "proyectofinalpcd-816d5.appspot.com",
  "messagingSenderId": "341285184166",
  "appId": "1:341285184166:web:988dd980f771f7b150ca67",
  "measurementId": "G-6DE3ERD9GD"
}
firebase = pb.initialize_app(firebaseConfig)

db = firebase.database()
all_users = db.child("Usuarios").get()
#contadores
pauta_completa=0
pauta_incompleta=0
alumnos=0

print(all_users.val)
# contar el numero de Alumnos con info adecuada

for users in all_users.each():
        if 'Dosis' in str(users.val()):
            
            users_by_dosis = db.child("Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/Dosis").get()
            alumnos+=1
            users_by_dosis_suministradas = db.child("Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/Vacunas_suministradas").get()

            print(str(users_by_dosis.key() + ': ') + str(users_by_dosis.val()))
            if int(users_by_dosis_suministradas.val())==users_by_dosis.val():
                pauta_completa += 1
            else:
                pauta_incompleta += 1
# Alumnos con Pauta completa
print("nombre de Alumnos con pauta completa: ",pauta_completa)

# Alumnos con pauta incompleta
print("nombre de Alumnos con pauta incompleta: ",pauta_incompleta)

# Total de alumnos vacunados
print("nombre de Alumnos vacunados: ",alumnos)

# diferencia entre alumnos de pauta completa y de pauta incompleta
import pandas as pd
import altair as alt

source = pd.DataFrame({"category": ["pauta completa", "pauta incompleta"], "value": [pauta_completa,pauta_incompleta]})

alt.Chart(source).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="category", type="nominal"),
)

# segundo diagrama que presenta el n_alumnos de pauta completa, pauta incompleta y total de alumnos vacunados
import plotly.graph_objects as go
fig = go.Figure(go.Bar(
            x=[pauta_completa,pauta_incompleta ,alumnos],
            y=['n_alumnos pauta completa', 'n_alumnos pauta incompleta', 'total de alumnos '],
            orientation='h'))

fig.show()
