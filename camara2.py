import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
tomar_foto=st.button('Tomar foto')
while run:
    _,frame = camera.read()
    _,imagen = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGRA)

    FRAME_WINDOW.image(frame)

    if tomar_foto:
        img_name = "fotoPersona.png"
        #img2 = cv2.read(imagen)
        cv2.imwrite(img_name, imagen)
        #cv2.imwrite(img_name, cv2.cvtColor(img, cv2.COLOR_BGRA2RGB))
        print("fotoPersona.png written!")
        break
else:
    st.write('Stopped')