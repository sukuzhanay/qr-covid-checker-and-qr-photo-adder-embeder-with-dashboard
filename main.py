import pandas as pd
import pyrebase as pb
import streamlit as st
import datetime as dt
from datetime import date
from datetime import timedelta
import plotly.graph_objects as go
import altair as alt

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
}

firebase = pb.initialize_app(firebaseConfig)
sign_in_up = firebase.auth()
dd_bb = firebase.database()
# Login
mail = "lembajosa@gmail.com"
password = "patata123"
user = sign_in_up.sign_in_with_email_and_password(mail, password)


def date_range(start, end):
    delta = end - start
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return delta.days


def tiempo_medio(localId):
    # De momento se le pide al usuario el identificador, sin embargo esto se tiene que autocompletar una vez inice
    all_users = dd_bb.child("Usuarios").get()
    # Se obtiene la fecha de vacunacion del usuario
    ult_vacuna = dd_bb.child("Usuarios/" + localId + "/Datos_de_vacunacion/Fecha_de_Vacunación").get()

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
                _meses_pasados = meses_pasados - 12
                if _meses_pasados == 1:
                    df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [
                        str(anios) + " año " + str(meses_pasados - 12) + " mes"]})

                else:
                    df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [
                        str(anios) + " año " + str(meses_pasados - 12) + " meses"]})

            else:
                _meses_pasados = meses_pasados - 12
                if _meses_pasados == 1:
                    df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [
                        str(anios) + " años " + str(meses_pasados - 12) + " mes"]})

                else:
                    df = pd.DataFrame({"Tiempo medio desde la ultima vacunacion": [
                        str(anios) + " años " + str(meses_pasados - 12) + " meses"]})

    st.table(df)


def periodo_vacunacion():
    # Se obtienen todos los usuarios
    all_users = dd_bb.child("Usuarios").get()
    # Fecha actual
    tiempo_actual = date.today()

    x = []
    y = []

    # Variables donde se guardaran los resultados
    unoMeses = 0
    tresMeses = 0
    seisMeses = 0
    nueveMeses = 0
    doceMeses = 0
    quinceMeses = 0

    contador = 0
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
            elif 1 <= meses_pasados <= 2:
                unoMeses += 1
            elif 3 <= meses_pasados <= 5:
                tresMeses += 1
            elif 6 <= meses_pasados <= 8:
                seisMeses += 1
            elif 9 <= meses_pasados <= 11:
                nueveMeses += 1
            elif 12 <= meses_pasados <= 14:
                doceMeses += 1
            elif meses_pasados >= 15:
                quinceMeses += 1

            # Una vez terminada de sumar 1, en el mes correspondiente, se suma el contador y realiza lo mismo con los siguientes usaurios
            contador += 1

    # Se cargan los valores del grafico
    source = pd.DataFrame({
        'Tiempo transcurrido': ["1 meses", "3 meses", "6 meses", "9 meses", "12 meses", "15 meses"],
        'Número de personas': [unoMeses, tresMeses, seisMeses, nueveMeses, doceMeses, quinceMeses]
    })

    chart = alt.Chart(source).mark_bar(color='purple').encode(
        x=alt.X("Tiempo transcurrido:O", title="Tiempo Transcurrido",
                sort=["1 meses", "3 meses", "6 meses", "9 meses", "12 meses", "15 meses"]),
        y=alt.Y("Número de personas:Q", title="Número de personas", axis=alt.Axis(tickMinStep=1),
                scale=alt.Scale(domain=(0, contador + 1))),
    )

    st.altair_chart(chart)


def porcentaje_tipo_vacuna():
    spikevax = 0
    comirnaty = 0
    covishield = 0
    janssen = 0

    all_users = dd_bb.child("Usuarios").get()

    for users in all_users.each():
        if "Moderna" in str(users.val()):
            spikevax += 1
        elif "Comirnaty" in str(users.val()):
            comirnaty += 1
        elif "Covishield" in str(users.val()):
            covishield += 1
        else:
            janssen += 1

    print("Moderna " + str(spikevax) + "Comirnaty " + str(comirnaty) + "Covishield " + str(
        covishield) + "Janssen " + str(
        janssen))

    vacunas = ["Moderna", "Comirnaty", "Covishield", "Janssen"]
    valores = [spikevax, comirnaty, covishield, janssen]

    # ====== PIE CHART - TIPO VACUNAS =========
    fig = go.Figure(
        go.Pie(
            labels=vacunas,
            values=valores,
            hoverinfo="label+percent",
            textinfo="value"
        ))
    # fig.update_layout(
    #     autosize=True)
    #         width=500,
    #         height=500
    #     )
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=25)
    st.header("Vacunas")
    st.plotly_chart(fig)  # use_container_width=True
    # Grafica se pasa a Streamlit


# ============== Porcentaje vacunados =============

def porcentaje_pauta_completa():
    pauta_completa_bbdd = 0
    pauta_incompleta_bbdd = 0

    all_users = dd_bb.child("Usuarios").get()

    for users in all_users.each():
        if 'Dosis' in str(users.val()):
            users_by_dosis = dd_bb.child("Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/Dosis").get()
            users_by_dosis_suministradas = dd_bb.child(
                "Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/Vacunas_suministradas").get()

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
    fig.update_traces(hoverinfo='label+value', textinfo='percent+label',
                      marker=dict(colors=color_pauta, line=dict(color='#000000')))
    # fig.update_layout(
    #     autosize=True)
    #     width=500,
    #     height=500
    # )
    fig.update_yaxes(automargin=True)
    st.header("Pauta de vacunación")
    st.plotly_chart(fig)  # use_container_width=True)


def pauta_media():
    all_users = dd_bb.child("Usuarios").get()
    # contadores
    pauta_completa = 0
    pauta_incompleta = 0
    alumnos = 0

    # contar Alumnos con info adecuada

    for users in all_users.each():
        if 'Dosis' in str(users.val()):

            users_by_dosis = dd_bb.child("Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/Dosis").get()
            alumnos += 1
            users_by_dosis_suministradas = dd_bb.child(
                "Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/Vacunas_suministradas").get()

            print(str(users_by_dosis.key() + ': ') + str(users_by_dosis.val()))
            if int(users_by_dosis_suministradas.val()) == users_by_dosis.val():
                pauta_completa += 1
            else:
                pauta_incompleta += 1
    # Alumnos con Pauta completa
    print("nombre de Alumnos con pauta completa: ", pauta_completa)

    # Alumnos con pauta incompleta
    print("nombre de Alumnos con pauta incompleta: ", pauta_incompleta)

    # Total de alumnos vacunados
    print("nombre de Alumnos vacunados: ", alumnos)

    source = pd.DataFrame(
        {"category": ["pauta completa", "pauta incompleta"], "value": [pauta_completa, pauta_incompleta]})

    alt.Chart(source).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="value", type="quantitative"),
        color=alt.Color(field="category", type="nominal"),
    )
    z = [pauta_completa, pauta_incompleta]
    colors = 'crimson'
    # segundo diagrama que presenta el n_alumnos de pauta completa, pauta incompleta y total de alumnos vacunados
    fig = go.Figure(go.Bar(
        x=z,
        y=['n_alumnos pauta completa', 'n_alumnos pauta incompleta'],
        text=z,
        marker_color='rgb(255, 40, 0)',
        textposition='auto',
        orientation='h'))


    fig.update_layout(
        xaxis=dict(
            title='Numero Total de Registrados',
        )
    )


    st.plotly_chart(fig)


def vacunados_mes():
    # Se obtienen todos los usuarios
    all_users = dd_bb.child("Usuarios").get()

    x = []
    y = []

    enero = 0
    febrero = 0
    marzo = 0
    abril = 0
    mayo = 0
    junio = 0
    julio = 0
    agosto = 0
    septiembre = 0
    octubre = 0
    noviembre = 0
    diciembre = 0

    contador = 0

    for users in all_users.each():
        if 'Fecha_de_Vacunación' in str(users.val()):
            ult_vacuna = dd_bb.child("Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/Fecha_de_Vacunación").get()
            # Las fechas se guardan en un array
            x.append(ult_vacuna.val())
            # Se guarda en y la fecha dividida con el split
            y = str(x[contador]).split("-")

            mes_vacuna = int(y[1])
            print(mes_vacuna)
            if mes_vacuna == 1:
                enero += 1
            elif mes_vacuna == 2:
                febrero += 1
            elif mes_vacuna == 3:
                marzo += 1
            elif mes_vacuna == 4:
                abril += 1
            elif mes_vacuna == 5:
                mayo += 1
            elif mes_vacuna == 6:
                junio += 1
            elif mes_vacuna == 7:
                julio += 1
            elif mes_vacuna == 8:
                agosto += 1
            elif mes_vacuna == 9:
                septiembre += 1
            elif mes_vacuna == 10:
                octubre += 1
            elif mes_vacuna == 11:
                noviembre += 1
            elif mes_vacuna == 12:
                diciembre += 1

            contador += 1

    source = pd.DataFrame({
        'Mes': ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
                "noviembre", "diciembre"],
        'Personas/mes': [enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre,
                         diciembre]
    })

    chart = alt.Chart(source).mark_bar(color='purple').encode(
        x=alt.X("Mes:O", title="Mes",
                sort=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
                      "noviembre", "diciembre"]),
        y=alt.Y("Personas/mes:Q", title="Personas/mes", axis=alt.Axis(tickMinStep=1),
                scale=alt.Scale(domain=(0, contador + 1))),
    )
    st.altair_chart(chart)


#c = st.container()
#with c:
#    pauta_media()
#    porcentaje_tipo_vacuna()
#    porcentaje_pauta_completa()
#
# col2, col3 = st.columns(2)
# with col2:
#     tiempo_medio()
# with col3:
#     periodo_vacunacion()
#     vacunados_mes()
