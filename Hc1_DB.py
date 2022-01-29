import pyrebase as pb
import json
import base45 #pip install base45
import cbor2 #pip install cbor2
import zlib

class BBDD():
    def __init__(self):
        self.firebaseConfig = {
          "apiKey": "AIzaSyArmVriibDlBkIJ_3yURB1e3QprmU1z3hY",
          "authDomain": "proyectofinalpcd-816d5.firebaseapp.com",
          "databaseURL": "https://proyectofinalpcd-816d5-default-rtdb.europe-west1.firebasedatabase.app/",
          "projectId": "proyectofinalpcd-816d5",
          "storageBucket": "proyectofinalpcd-816d5.appspot.com",
         "messagingSenderId": "341285184166",
          "appId": "1:341285184166:web:988dd980f771f7b150ca67",
          "measurementId": "G-6DE3ERD9GD"
        }
        self.firebase=pb.initialize_app(self.firebaseConfig)  
        self.ddbb=self.firebase.database()



  def autenticacion(self):
        sign_in_up = self.firebase.auth()  # inicio de sesion
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