import pyrebase as pb
import json
import base45 #pip install base45
import cbor2 #pip install cbor2
import zlib

##############################################################################################################################################
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
        
    
    def decode(self,hc1_decodificado):
        b45data = hc1_decodificado.replace("HC1:", "")
        zlibdata = base45.b45decode(b45data)
        cbordata = zlib.decompress(zlibdata)
        decoded = cbor2.loads(cbordata)
        self.data = cbor2.loads(decoded.value[2])
        
        self.save_storage()
        self.guardarDatos()
        
        
    def get_fullname(self):
        name = self.data[-260][1]["nam"]["gn"]
        name = name.replace(" ", "_")
        surname = self.data[-260][1]["nam"]["fn"]
        surname = surname.replace(" ", "_")
        return name + "_" + surname
    
    def save_storage(self):
        json_name = self.get_fullname()+".json"
        print(json_name)
        with open("sample.json", "w") as outfile:
            self.jsonData = json.dump(self.data, outfile)
        outfile.close()
        patata = "sample.json"
        self.storage.child("archivos/" + json_name).put(patata)
        print(len(json_name))
      

    
    
    ##############################################################################################################################################
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
    
    ##############################################################################################################################################
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
        
    ##############################################################################################################################################
    def recuperar_datos_vacunas(self):
        self.datadir = 'https://console.firebase.google.com/project/proyectofinalpcd-816d5/storage/proyectofinalpcd-816d5.appspot.com/files/~2Farchivos'
        self.storage.child('archivos/vacunas.json').download(self.datadir,'vacunas.json')
        self.storage.child('archivos/Fabricante.json').download(self.datadir,'Fabricante.json')
        self.storage.child('archivos/profilaxis.json').download(self.datadir,'profilaxis.json')
        
    def nombre_vacuna(self,mp):
        with open('vacunas.json') as vacunas:
            json_vacuna = json.load(vacunas)
        for key in json_vacuna["valueSetValues"]:
            if (key==mp):
                vacuna = json_vacuna["valueSetValues"][key]['display']
                print(vacuna)
        return vacuna
    
    def fabricante_vacuna(self,ma):
        with open('Fabricante.json') as fabricante:
            json_fabricante = json.load(fabricante)
        for key in json_fabricante["valueSetValues"]:
            if (key==ma):
                fabricante = json_fabricante["valueSetValues"][key]['display']
                print(fabricante)
        return fabricante
    
    def tipo_vacuna(self,vp):
        with open('profilaxis.json') as profilaxis:
            json_profilaxis = json.load(profilaxis)
        for key in json_profilaxis["valueSetValues"]:
            if (key==vp):
                tipoVacuna = json_profilaxis["valueSetValues"][key]['display']
                print(tipoVacuna)
        return tipoVacuna
    
    
    
    ##############################################################################################################################################
    
    def guardarDatos(self):
        self.recuperarDatos()#self.issuer
        self.recuperar_datos_vacunas()
        VacunaAdministrada = self.nombre_vacuna(self.mp)
        fabricante = self.fabricante_vacuna(self.ma)
        tipoVacuna = self.tipo_vacuna(self.vp)
        db = {
            "Apellidos":self.fn,
            "Nombre":self.gn,
            "Datos_de_vacunacion":{
                "ID_vacunacion":self.ci,
                "Emisor_certificado":self.issuer,
                "Enfermedad":self.tg,
                "Fecha_de_Vacunación":self.date,
                "Vacunas_suministradas":self.num_dosis,
                "Dosis":self.sd,
                "Pais":self.pais,
                "Tipo_de_vacuna":tipoVacuna,
                "Vacuna_subministrada":VacunaAdministrada,
                "Fabricante":fabricante
            }
        }
        
        all_users = self.ddbb.child("Usuarios").get()
        verif = False
        for users in all_users.each():
            if 'ID_vacunacion' in str(users.val()):
                vac = self.ddbb.child("Usuarios/" + str(users.key()) + "/Datos_de_vacunacion/ID_vacunacion").get()
                if (vac.val()==self.ci):
                    verif = True
                    print("Entro")
                    self.ddbb.child("Usuarios/" + str(users.key())).update(db)
        if (verif == False):
            self.ddbb.child("Usuarios").push(db)
                    
    
    ##############################################################################################################################################
s = BBDD()
hc1_code = "HC1:NCFOXN%TSMAHN-HPQCXAV03C1KK%%V:D4%X4-36QHN-TMOV4+HH8UO7/IJ8W1-NNO4*J8OX4W$C2VLWLIVO5ON1: BI$H1VOZ0QD:RHQ1NYJRT1 V1.GO$HQ0IQ-88IV4/974CL395J4I-B5ET42HPPEPHCRBK8MDPAC5LGN1:6G16PCNQ+MBM6P846$AU47N/5QV4IV4:/6N9R%EPL8RU9DNKM*IK5C9A.D90I/EL6KKYHIF.70A90%KLR2A KZ*U0I1-I0*OC6H0/VMNPM Q5TM8*N9 I2.8Q4A7E:7LYPFTQ7XBEEOPCRQQ5L/5R3FMIAC/BG9MS7K0RDHJ8LUKLTHVPC9JAP.B*EM95E:UL0NG-QD78KS7K15G4JB381.$IYTABLE/*BCVA0V1DDB$JDVPLZ2KD0KJWGN 9X$PO7OUNUC0QEQL4DJIPT3SQ%L3K/AWOH.ZLOWVN240MN./UN$5PPE9JH:+3N7WQALM4DT7N +B7HFLHAS7OXZUUBK/89:05+VT2OJPYF"
s.decode(hc1_code)