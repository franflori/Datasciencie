import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
st.title("Main Page")
st.sidebar.success("Select a page above")

if "mi_input" not in st.session_state:
    st.session_state["mi_input"] = ""

my_input=st.text_input("Input a text here"), st.session_state["mi_input"] 
submit= st.button("Submin")
if submit:
    st.session_state["mi_input"]= my_input
    st.write(" has puslasdo", my_input)