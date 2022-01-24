import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
tomar_foto=st.button('Tomar foto')
while run:
    _,frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    if tomar_foto:
        img_name = "fotoPersona.png"
        cv2.imwrite(img_name, frame)
        print("fotoPersona.png written!")
        break
else:
    st.write('Stopped')