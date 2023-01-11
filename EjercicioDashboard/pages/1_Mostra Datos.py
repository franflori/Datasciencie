import streamlit as st
from datos_get import Datos_get
import seaborn as sns
import matplotlib.pyplot as plt
from grafico import Grafico
import pandas as pd


from plotnine import *


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
    st.title("Datos de la pantal")

    # head()
    st.write("Vamos a imprimir los valores del dataset")
    st.write(df)

    




pintarDatos()

pintarGrafico=Grafico()
cadena=["Pclass", "Sex", "Age","SibSp","Parch","Fare",
                            "Embarked"]
pintarGrafico.iniciaGraficios(cadena,df,True)
pantalla.pulsaPrepocesar()

#pintarGrafico.histrogama(df.Sex)

#pintarGrafico.violinplot3("Embarked","Pclass","Sex","Age","Survived",df)

#for column in df:
#    print(column)



 # state_total_graph = px.bar(
  #      state_total, 
  #      x='Status',
  #      y='Number of cases',
  #      labels={'Number of cases':'Number of cases in %s' % (select)},
  #      color="Status")
  #st.plotly_chart(state_total_graph)


#fig, ax = plt.subplots()
#pd.crosstab(df.Pclass, df.Survived).plot(kind="bar")
#st.pyplot(fig)

#fig, ax = plt.subplots()
#sns.catplot(x="Sex", y="Survived", hue="Pclass", kind="point", height=4, aspect=2, data=df)
#st.pyplot(fig)









