import pyrebase as pb
import streamlit as st
import plotly.graph_objects as go

# ¡¡¡API DE PRUEBA - base de datos falsa!!!
firebaseConfig = {
    "apiKey": "AIzaSyArmVriibDlBkIJ_3yURB1e3QprmU1z3hY",
    "authDomain": "proyectofinalpcd-816d5.firebaseapp.com",
    "databaseURL": "https://proyectofinalpcd-816d5-default-rtdb.europe-west1.firebasedatabase.app/",
    "projectId": "proyectofinalpcd-816d5",
    "storageBucket": "proyectofinalpcd-816d5.appspot.com",
    "messagingSenderId": "341285184166",
    "appId": "1:341285184166:web:988dd980f771f7b150ca67",
    "measurementId": "G-6DE3ERD9GD"
}

firebase = pb.initialize_app(firebaseConfig)
sign_in_up = firebase.auth()
# Login de prueba
mail = "mtrgomez00@gmail.com"
passw = "12345678"
user = sign_in_up.sign_in_with_email_and_password(mail, passw)
db = firebase.database()

all_users = db.child("Usuarios").get()


# =========== Contador de tipos de vacuna =================

def porcentaje_tipo_vacuna():
    spikevax = 0
    comirnaty = 0
    covishield = 0
    janssen = 0

    for users in all_users.each():
        if "Spikevax" in str(users.val()):
            spikevax += 1
        elif "Comirnaty" in str(users.val()):
            comirnaty += 1
        elif "Covishield" in str(users.val()):
            covishield += 1
        else:
            janssen += 1

    print("Spikevax " + str(spikevax) + "Comirnaty " + str(comirnaty) + "Covishield " + str(
        covishield) + "Janssen " + str(
        janssen))

    vacunas = ["Spikevax", "Comirnaty", "Covishield", "Janssen"]
    valores = [spikevax, comirnaty, covishield, janssen]

    # ====== PIE CHART - TIPO VACUNAS =========
    fig = go.Figure(
        go.Pie(
            labels=vacunas,
            values=valores,
            hoverinfo="label+percent",
            textinfo="value"
        ))
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=20)

    # Grafica se pasa a Streamlit
    st.header("Vacunas")
    st.plotly_chart(fig)


# ============== Porcentaje vacunados =============

def porcentaje_pauta():
    pauta_completa = 0
    pauta_incompleta = 0

    for users in all_users.each():
        if 'dosis' in str(users.val()):
            users_by_dosis = db.child("users/" + str(users.key()) + "/dosis").get()
            print(str(users_by_dosis.key() + ': ') + str(users_by_dosis.val()))
            if int(users_by_dosis.val()) > 1:
                pauta_completa += 1
            else:
                pauta_incompleta += 1

    print(pauta_completa)
    print(pauta_incompleta)
    # ====== PIE CHART - PORCENTAJE DOSIS =========

    color_pauta = ['green', 'darkorange']
    labels = ['Pauta completa', '1 dosis']
    values = [pauta_completa, pauta_incompleta]

    # Use `hole` to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=20,
                      marker=dict(colors=color_pauta, line=dict(color='#000000', width=2)))
    st.header("Pauta de vacunación")
    st.plotly_chart(fig)


# Para la base de datos oficial
def porcentaje_pauta_completa():
    pauta_completa_bbdd = 0
    pauta_incompleta_bbdd = 0

    for users in all_users.each():
        if 'Dosis' in str(users.val()):
            users_by_dosis = db.child("Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/Dosis").get()
            users_by_dosis_suministradas = db.child("Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/Vacunas_suministradas").get()

            print(str(users_by_dosis.key() + ': ') + str(users_by_dosis.val()))
            print(str(users_by_dosis_suministradas.key() + ': ') + str(users_by_dosis_suministradas.val()))
            if str(users_by_dosis.val()) == str(users_by_dosis_suministradas.val()):
                pauta_completa_bbdd += 1
            else:
                pauta_incompleta_bbdd += 1

    print(pauta_completa_bbdd)
    print(pauta_incompleta_bbdd)
    # ====== PIE CHART - PORCENTAJE DOSIS =========

    color_pauta = ['green', 'darkorange']
    labels = ['Pauta completa', 'Pauta incompleta']
    values = [pauta_completa_bbdd, pauta_incompleta_bbdd]

    # Use `hole` to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_traces(hoverinfo='label+value', textinfo='percent+label', textfont_size=20,
                      marker=dict(colors=color_pauta, line=dict(color='#000000', width=2)))
    st.header("Pauta de vacunación")
    st.plotly_chart(fig)


porcentaje_tipo_vacuna()
porcentaje_pauta_completa()
