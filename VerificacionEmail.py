import pyrebase as pb
import socket
import pandas as pd, numpy as np

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

   firebase=pb.initialize_app(firebaseConfig)  
ddbb=firebase.database()
sign_in_up=firebase.auth()  # inicio de sesion
email=input("Introduzca su email")
contrasenia = input("Introduzca su contraseña")
try:
    user = sign_in_up.create_user_with_email_and_password(email, contrasenia) # da de alta el email y la contra
    Token = user.get("idToken") # genera el token del usuario
    sign_in_with_token = sign_in_up.send_email_verification(Token) # verificacion enviada al email
except:
    try:
        user = sign_in_up.sign_in_with_email_and_password(email, contrasenia)
        Token = user.get("idToken") # genera el token del usuario
    except:
        print("Contraseña incorrecta")

storage = firebase.storage()
datadir = 'https://console.firebase.google.com/project/proyectofinalpcd-816d5/storage/proyectofinalpcd-816d5.appspot.com/files/~2Farchivos'
storage.child('archivos/data').download(datadir,'data1.json')
with open('data1.json') as file:
    data = json.load(file)

ci =data['Data']["value"][3][1]["value"][0][1]["v"][0]["ci"]
pais=data['Data']["value"][3][1]["value"][0][1]["v"][0]["co"]
num_dosis=data['Data']["value"][3][1]["value"][0][1]["v"][0]["dn"]
date=data['Data']["value"][3][1]["value"][0][1]["v"][0]["dt"]
ma = data['Data']["value"][3][1]["value"][0][1]["v"][0]["ma"]
mp = data['Data']["value"][3][1]["value"][0][1]["v"][0]["mp"]
sd = data['Data']["value"][3][1]["value"][0][1]["v"][0]["sd"]
tg = data['Data']["value"][3][1]["value"][0][1]["v"][0]["tg"]
vp = data['Data']["value"][3][1]["value"][0][1]["v"][0]["vp"]
dob = data['Data']["value"][3][1]["value"][0][1]["dob"]
fn = data['Data']["value"][3][1]["value"][0][1]["nam"]["fn"]
gn = data['Data']["value"][3][1]["value"][0][1]["nam"]["gn"]
fnt = data['Data']["value"][3][1]["value"][0][1]["nam"]["fnt"]
gnt = data['Data']["value"][3][1]["value"][0][1]["nam"]["gnt"]
issuer = data['Data']["value"][3][1]["value"][0][1]["v"][0]["is"]



vacunas = pd.read_excel('Vacunas.xlsx')
vacunas = vacunas.to_numpy()
for i in range (len(vacunas)):
    if(vacunas[i][2] == mp): # mp es el org
        tipoVacuna = vacunas[i][3]
        fabricante = vacunas[i][1]
        VacunaAdministrada = vacunas[i][0]
db = {
            "Apellidos":gn,
            "Nombre": fn,
            "Datos de vacunacion":{
                "Emisor certificado":issuer,
                "Enfermedad":tg,
                "Fecha de Vacunación":date,
                "Vacunas suministradas":num_dosis,
                "Dosis":sd,
                "Pais":pais,
                "Tipo de vacuna":tipoVacuna,
                "Vacuna subministrada":VacunaAdministrada,
                "Fabricante":fabricante
    }

}
ddbb.child("Usuarios").push(db1)