import streamlit as st

st.title("Cargar Datos")
if "mi_input"  in st.session_state:
    st.write("tu has escrito,", st.session_state["mi_input"])
