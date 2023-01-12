
import streamlit as st
from datos_get import Datos_get


st.set_page_config(
    page_title="Estudio Proyecto Titanic ",
    page_icon="👋",
)

st.header("Inicio del estudio")

st.markdown('Se va realizar un Dashboard usando Streamlit para visualizar y predecir la información presente en un dataset.')
 
st.markdown('El dataset utilizado sera **Titanic**')

st.markdown('Se puede observar hay diferentes opcines de menu ')

st.markdown("1. **Mostar datos** se va a mostrar los datos de titanic y se permitira crear diferentes graficos con los datos del Dataset")

st.markdown("2. **Filtrar** se permite filtra por diferentes campos, se mostrara los datos filtrados y las diferentes graficas con esos datos filtrados")

st.markdown("3. **Preprocesar** En esto datos se modifica el dataset, para que se pueda realizar facilmente el estudio, se mostrara los datos modificados con las diferetnes graficas")

st.markdown("4. **Entrenamiento** con los datos ya modificados se muestra los resutaldos de los diferentes algoritmo se mostrara los diferentes algorimos")

st.markdown("5. **Predicion** se introducira los datos de un nuevo pasajero y con los datos introducidos se va predicir si el pasajero sobrevivio o fallecio en el titanic")

st.markdown("6. **Guardar** Se Almacenarán los datos que nos den los usuarios, para ir enriqueciendo nuestros datos.")
st.markdown("")
st.markdown("")
st.markdown("Creado por")
st.markdown("**Francisco Javier Florido**")


df=Datos_get().read_datos()


if "df_datos" not in st.session_state:
    st.session_state["df_datos"] = ""
st.session_state["df_datos"]= df


