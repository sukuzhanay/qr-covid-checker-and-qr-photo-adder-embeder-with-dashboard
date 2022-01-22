import pyrebase as pb
import streamlit as st
import pandas as pd
firebaseConfig = {
  "apiKey": "AIzaSyBsyBZDG0BF6F9BAi95G_bW_wVP3xt7_sc",
  "authDomain": "pcd-prueba.firebaseapp.com",
  "databaseURL": "https://pcd-prueba-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "pcd-prueba",
  "storageBucket": "pcd-prueba.appspot.com",
  "messagingSenderId": "547368512451",
  "appId": "1:547368512451:web:e7e22f6f578c608651ab76"
}
firebase = pb.initialize_app(firebaseConfig)
db = firebase.database()
all_users = db.child("users").get()

pauta_completa=0
pauta_incompleta=0
alumnos=0

print(all_users.val)

# contar Alumnos con info adecuada
for users in all_users.each():
    if 'dosis' in str(users.val()):
        
        users_by_dosis = db.child("users/" + str(users.key()) + "/dosis").get()
        alumnos+=1
        print(str(users_by_dosis.key() + ': ') + str(users_by_dosis.val()))
        if int(users_by_dosis.val()) > 1:
            pauta_completa += 1
        else:
            pauta_incompleta += 1
			
def pautaCompleta():
    pourcentaje1=(pauta_completa/3)*100
    print("pourcentaje de alumnos que tengan pauta completa= ",pourcentaje1,"%")
def pautaIncompleta():
    pourcentaje2=(pauta_incompleta/alumnos)*100
    print("pourcentaje de alumnos que tengan pauta completa= ",pourcentaje2,"%")

# percentaje pauta completa
pautaCompleta()

# percentaje pauta incompleta
pautaIncompleta()


import streamlit as st
import pandas as pd
import altair as alt
import pandas as pd
pourcentaje11=(pauta_incompleta/alumnos)*100
pourcentaje22=(pauta_completa/alumnos)*100
source = pd.DataFrame({
    'a': ['una dosis', 'dos dosis'],
    'b': [pourcentaje11, pourcentaje22]
})

alt.Chart(source).mark_bar().encode(
    x='a',
    y='b'
)
