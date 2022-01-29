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
        self.storage = self.firebase.storage()
        hc1_code = "HC1:NCFOXN%TSMAHN-HXOCLGML-P8ZVHGJ-AH:TA1ROT$SD PLIS2VF%GKG5/E71F/8XG3M9JUPY0BZW4V/AY73CNN7J3J1H:43DAJBRNFG3CNBRI3CHG7KM0KLGJJ5C9-JE%7A6IA$36IASD9YHILIIX2MELNKHKYIARGEX3E1.BLEE$JDM:C5H8QNL1FE1.B7I9 H9/.DV2MGDIR0MTDQVOCIL8-TIKR3T3+7A.N88J4R$FBMA2 U6QS25P0QIRR97I2HOAAP9UY9VYCDEBD0HX2JR$4O1K8KES/F-1JZ.KELNZEG%12/9TL4T.B9 UP9C1-ZEN.HQCEFREGUA P1NV1K/U31AP8Q0OE+51QN1RNU.*U-51JFEKQU2:UWH9 UPRB8LTD1$AZWJYQ2%VLUHGG%5TW5A 6+O67N6F7E46WW%9Z4EM2PKAWMO9T.3NB1E7R0%K06N0%8/YM.QPMSD9IM28K/NS /K%TTVP5TPTT$CKTMS MKCHK+RO2W58ECQ568HX%A+YP8MAKL62QG"



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
                
                
    def recuperarDatos(self):
        self.ci = self.data[-260][1]["v"][0]["ci"]
        self.pais = self.data[-260][1]["v"][0]["co"]
        self.num_dosis = self.data[-260][1]["v"][0]["dn"]
        self.date = self.data[-260][1]["v"][0]["dt"]
        self.ma = self.data[-260][1]["v"][0]["ma"]
        self.mp = self.data[-260][1]["v"][0]["mp"]
        self.issuer = self.data[-260][1]["v"][0]["is"]
        self.sd = self.data[-260][1]["v"][0]["sd"]
        self.tg = self.data[-260][1]["v"][0]["tg"]
        self.vp = self.data[-260][1]["v"][0]["vp"]
        self.dob = self.data[-260][1]["dob"]
        self.fn = self.data[-260][1]["nam"]["fn"]
        self.gn = self.data[-260][1]["nam"]["gn"]
        self.fnt = self.data[-260][1]["nam"]["fnt"]
        self.gnt = self.data[-260][1]["nam"]["gnt"]