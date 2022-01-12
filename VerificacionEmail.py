import pyrebase as pd
import socket

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

   firebase=pd.initialize_app(firebaseConfig)  
ddbb=firebase.database()
sing_in_up=firebase.auth()  # inicio de sesion
email=input("Introduzca su email")
contrasenia = input("Introduzca su contraseña")
user = sing_in_up.create_user_with_email_and_password(email, contrasenia) # da de alta el email y la contra
Token = user.get("idToken") # genera el token del usuario
sign_in_with_token = sing_in_up.send_email_verification(Token) # verificacion enviada al email