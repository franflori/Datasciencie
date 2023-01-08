import streamlit as st
from datos_get import Datos_get
import seaborn as sns
import matplotlib.pyplot as plt

from pantalla import Pantalla

st.title("Cargar Datos")
df=Datos_get().read_datos()


if "df_datos" not in st.session_state:
    st.session_state["df_datos"] = ""




st.session_state["df_datos"]= df

if "pantalla" not in st.session_state:
    st.session_state["pantalla"] = ""

pantalla= Pantalla()
st.session_state["pantalla"] = pantalla

def pintarDatos():
    st.title("Gráfica con Streamlit .............s")

    # head()
    st.write("Vamos a imprimir los primeros 5 valores del dataset")
    st.write(df.head())

    # tail()
    st.write("Vamos a imprimir los últimos 5 valores del dataset")
    st.write(df.tail())


pintarDatos()
fig, ax = plt.subplots()
    
ax.hist(df.Sex)
st.pyplot(fig)

   

   

    
    # me creo una figura
fig= plt.figure()
    # 3 subplots
    # 1 fila 3 columnas - gráfica 1
ax1 = fig.add_subplot(131)
    # 1 fila 3 columnas - gráfica 2
ax2 = fig.add_subplot(132)
    # 1 fila 3 columnas - gráfica 3
ax3 = fig.add_subplot(133)
    # violinplot
sns.violinplot(x="Embarked", y="Age", hue="Survived", data=df, ax=ax1)
sns.violinplot(x="Pclass", y="Age", hue="Survived", data=df, ax=ax2)
sns.violinplot(x="Sex", y="Age", hue="Survived", data=df, ax=ax3)
   
  
st.pyplot(fig)

#Histogramas con Seaborn
#sns_hist=sns.histplot(data=ds_trabajo['Age'], alpha = 0.5).set(title="Distribución de edades de pasajeros",xlabel="Age",ylabel="Frecuencia")