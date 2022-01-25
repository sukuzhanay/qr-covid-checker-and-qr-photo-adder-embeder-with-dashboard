# Modules
import pyrebase as pb
import streamlit as st
import cv2

# Datos de Firebase
firebaseConfig = {
    'apiKey': "AIzaSyArmVriibDlBkIJ_3yURB1e3QprmU1z3hY",
    'authDomain': "proyectofinalpcd-816d5.firebaseapp.com/",
    'projectId': "proyectofinalpcd-816d5",
    'databaseURL': "https://proyectofinalpcd-816d5-default-rtdb.europe-west1.firebasedatabase.app",
    'storageBucket': "proyectofinalpcd-816d5.appspot.com",
    'messagingSenderId': "341285184166",
    'appId': "1:341285184166:web:988dd980f771f7b150ca67",
    'measurementId': "G-6DE3ERD9GD"
}

# Iniciamos Firebase y autenticamos
firebase = pb.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()
st.sidebar.title("QRCovid")

# Menu desplegable
menu = st.sidebar.selectbox('Entrar/Registrar', ['Entrar', 'Registrar'])

# Pedimos usuario y contraseña
email = st.sidebar.text_input('Por favor, introduce tu email')
password = st.sidebar.text_input('Por favor, introduce tu contraseña', type='password')


# Registrar
if menu == 'Registrar':
    username_ = st.sidebar.text_input(
        'Introduce tu nombre ', value='QRCovid')
    lastname_ = st.sidebar.text_input(
        'Introduce tu apellido', value='QRCovid')
    crear_cuenta_button = st.sidebar.button('Crear cuenta')

    if crear_cuenta_button:
        if len(password) < 6:
            st.info('La contraseña debe incluir mas de 6 caracteres')
        else:
            #Creamos al usuario
            user = auth.create_user_with_email_and_password(email, password)
            st.success('Cuenta creada!')
            st.balloons() #Decoracion

            # Verificamos al usuario y añadimos datos en la db
            user = auth.sign_in_with_email_and_password(email, password)
            db.child('Usuarios').child(user['localId']).child("Nombre").set(username_) #LocalId lo crea Pyrebase
            db.child('Usuarios').child(user['localId']).child("Apellidos").set(lastname_)
            db.child('Usuarios').child(user['localId']).child("ID").set(user['localId'])
            st.title('Bienvenido ' + username_)

# Login
if menu == 'Entrar':
    login = st.sidebar.button('Entrar',key="3")
    if login:
        user = auth.sign_in_with_email_and_password(email, password)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        opciones = st.radio('Ir a', ['Home','Ajustes'],key="1")
        # Ajustes
        if opciones == 'Home':
            st.info('Aquí van los gráficos?')
        if opciones == 'Ajustes':
            st.info("No tienes foto aún")
            ''''# Comprobamos si el usuario tiene foto
            imagenes = db.child('Usuarios').child(user['localId']).child("Imagen").get().val()
            # Imagen encontrada
            if imagenes is not None:
                # Buscamos la imagen del usuario por su ID
                image_ = db.child('Usuarios').child(user['localId']).child("Imagen").get()
                for img in image_.each():
                    img_choice = img.val()
                st.image(img_choice)
                cambiar_foto = st.beta_expander('Cambia tu foto')
                # Cambiar imagen
                with cambiar_foto:
                    ruta_imagen = st.text_input('Introduce la ruta absoluta de tu imagen')
                    nueva_imagen = st.button('Cargar')
                    if nueva_imagen:
                        user_id = user['localId']
                        fireb_up = storage.child(user_id).put(ruta_imagen, user['idToken'])
                        img_url = storage.child(user_id).get_url(fireb_up['downloadTokens'])
                        db.child('Usuarios').child(user['localId']).child("Imagen").push(img_url)
                        st.success('Hecho!')
            # Imagen no encontrada
            else:'''

            '''ruta_imagen = st.text_input('Introduce la ruta absoluta de tu imagen')
            nueva_imagen = st.button('Cargar')
            tomar_foto = st.button('Tomar foto')
            if nueva_imagen:
                user_id = user['localId']
                fireb_up = storage.child(user_id).put(ruta_imagen, user['idToken'])
                img_url = storage.child(user_id).get_url(fireb_up['downloadTokens'])
                db.child('Usuarios').child(user_id).child('Imagen').push(img_url)
                st.success('Hecho!')
                if tomar_foto:
                    st.title("Es hora de tomarse una foto")
                    run = st.checkbox('Activar cámara')
                    FRAME_WINDOW = st.image([])
                    camera = cv2.VideoCapture(0)
                    tomar_imagen = st.button('Tomar foto')
                    while run:
                        _,frame = camera.read()
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        FRAME_WINDOW.image(frame)
                        if tomar_imagen:
                            img_name = "foto.png"
                            cv2.imwrite(img_name, frame)
                            st.info('Foto realizada! Guardando...')
                            break
                    else:
                        st.write('Cámara desactivada')'''
