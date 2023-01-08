import streamlit as st
from pantalla import Pantalla

st.title("Cargar Datos")
if "mi_input"  in st.session_state:
    st.write("tu has escrito,", st.session_state["mi_input"])
if "pantalla" not in st.session_state:
    st.session_state["pantalla"] = ""

pantalla= Pantalla()
st.session_state["pantalla"] = pantalla