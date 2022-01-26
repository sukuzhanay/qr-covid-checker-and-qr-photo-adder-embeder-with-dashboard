import streamlit as st
import base45
import cbor2
import zlib


#------------decoder function------------
def decoder(cert):
    b45data = cert
    zlibdata = base45.b45decode(b45data)
    cbordata = zlib.decompress(zlibdata)
    decoded = cbor2.loads(cbordata)
    return cbor2.loads(decoded.value[2])

#---------Streamlit----------
st.set_page_config(page_title="QR decoder", layout="wide")


#--Header--
st.subheader("HC1 decoder")
user_input = st.text_input("Insert your HC1 code here")

if user_input:  
    data = decoder(user_input) 
    st.write(data)






