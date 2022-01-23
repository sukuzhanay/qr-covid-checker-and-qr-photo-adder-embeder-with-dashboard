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
pauta_completa=0
pauta_incompleta=0
alumnos=0

print(all_users.val)
# contar Alumnos con info adecuada

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
# primer diagrama de pauta completa y incompleta
import pandas as pd
import altair as alt

source = pd.DataFrame({"category": ["pauta completa", "pauta incompleta"], "value": [pauta_completa,pauta_incompleta]})

alt.Chart(source).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="category", type="nominal"),
)

# segundo diagrama
import altair as alt
import pandas as pd

source = pd.DataFrame({
    'estado de vacunacion': [' pauta completa', ' pauta incompleta'],
    'total de alumnos': [pauta_completa,pauta_incompleta ]
})

alt.Chart(source).mark_bar().encode(
    x="estado de vacunacion",
    y="total de alumnos"
)
