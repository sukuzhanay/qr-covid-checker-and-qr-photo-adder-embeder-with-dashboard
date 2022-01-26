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
Data = {
  "dataType": "Map",
  "value": [
    [ 1, "ES" ],
    [ 4, 1685780100 ],
    [ 6, 1638619336 ],
    [
      -260,
      {
        "dataType": "Map",
        "value": [
          [
            1,
            {
              "v": [
                {
                  "ci": "01ES21VD3451FE17930000632516#4",
                  "co": "ES",
                  "dn": 1,
                  "dt": "2021-07-18",
                  "is": "Ministerio de sanidad",
                  "ma": "ORG-100031184",
                  "mp": "EU/1/20/1507",
                  "sd": 1,
                  "tg": "840539006",
                  "vp": "1119349007"
                }
              ],
              "dob": "1977-05-05",
              "nam": {
                "fn": "SUCUZHANAY AREVALO",
                "gn": "CHRISTIAN VLADIMIR",
                "fnt": "SUCUZHANAY<AREVALO",
                "gnt": "CHRISTIAN<VLADIMIR"
              },
              "ver": "1.3.0"
            }
          ]
        ]
      }
    ]
  ]
}
Id = (Data["value"][3][1]["value"][0][1]["v"][0]["ci"])
pais=(Data["value"][3][1]["value"][0][1]["v"][0]["co"])
num_dosis=(Data["value"][3][1]["value"][0][1]["v"][0]["dn"])
date=(Data["value"][3][1]["value"][0][1]["v"][0]["dt"])
ma = Data["value"][3][1]["value"][0][1]["v"][0]["ma"]
mp = Data["value"][3][1]["value"][0][1]["v"][0]["mp"]
sd = Data["value"][3][1]["value"][0][1]["v"][0]["sd"]
tg = Data["value"][3][1]["value"][0][1]["v"][0]["tg"]
vp = Data["value"][3][1]["value"][0][1]["v"][0]["vp"]
dob = Data["value"][3][1]["value"][0][1]["dob"]
fn = Data["value"][3][1]["value"][0][1]["nam"]["fn"]
gn = Data["value"][3][1]["value"][0][1]["nam"]["gn"]
fnt = Data["value"][3][1]["value"][0][1]["nam"]["fnt"]
gnt = Data["value"][3][1]["value"][0][1]["nam"]["gnt"]



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