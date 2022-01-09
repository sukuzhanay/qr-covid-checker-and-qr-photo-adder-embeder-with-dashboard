# Modules
import pyrebase as pb
import streamlit as st

# Datos de Firebase
firebaseConfig = {
    'apiKey': " ",
    'authDomain': " ",
    'projectId': " ",
    'databaseURL': " ",
    'storageBucket': " ",
    'messagingSenderId': "",
    'appId': " ",
    'measurementId': " "
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
        'Introduce tu nombre completo', value='QRCovid')
    crear_cuenta_button = st.sidebar.button('Crear cuenta')

    if crear_cuenta_button:
        #Creamos al usuario
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Cuenta creada!')
        st.balloons() #Decoracion

        # Verificamos al usuario y añadimos datos en la db
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Username").set(username_) #LocalId lo crea Pyrebase
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title('Bienvenido' + username_)

# Login
if menu == 'Entrar':
    login = st.sidebar.button('Entrar')
    if login:
        user = auth.sign_in_with_email_and_password(email, password)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        opciones = st.radio('Ir a', ['Ajustes'])

        # Ajustes
        if opciones == 'Ajustes':
            # Comprobamos si el usuario tiene foto
            imagenes = db.child(user['localId']).child("Imagen").get().val()
            # Imagen encontrada
            if imagenes is not None:
                # Buscamos la imagen del usuario por su ID
                image_ = db.child(user['localId']).child("Imagen").get()
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
                        db.child(user['localId']).child("Imagen").push(img_url)
                        st.success('Hecho!')
            # Imagen no encontrada
            else:
                st.info("No tienes foto aún")
                ruta_imagen = st.text_input('Introduce la ruta absoluta de tu imagen')
                nueva_imagen = st.button('Cargar')
                if nueva_imagen:
                    user_id = user['localId']
                    fireb_up = storage.child(user_id).put(ruta_imagen, user['idToken'])
                    img_url = storage.child(user_id).get_url(fireb_up['downloadTokens'])
                    db.child(user['localId']).child("Imagen").push(img_url)
                    st.success('Hecho!')