import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
class Grafico():


    def histrogama(self,campo):
       
        fig, ax = plt.subplots()
    
        ax.hist(campo)
        st.pyplot(fig) 



    def violinplotSencilo(self,ejex,ejey,valor,dato,ax):
       #fig,ax = plt.subplots()

        sns.violinplot(x=ejex, y=ejey, hue=valor, data=dato, ax=ax)
     
 
    def violinplot(self,ejex,ejey,valor,dato):
        
        fig= plt.figure()
        ax1 = fig.add_subplot(131)
       
        self.violinplotSencilo(ejex,ejey,valor,dato,ax1)
        

        st.pyplot(fig)

     
    def violinplot3(self,ejex1,ejex2,ejex3,ejey,valor,dato):
        
        fig= plt.figure()
        ax1 = fig.add_subplot(131)
        ax2 = fig.add_subplot(132)
        ax3 = fig.add_subplot(133)
        self.violinplotSencilo(ejex1,ejey,valor,dato,ax1)
        self.violinplotSencilo(ejex2,ejey,valor,dato,ax2)
        self.violinplotSencilo(ejex3,ejey,valor,dato,ax3)

        st.pyplot(fig)

    def funcion_graficas(self,feat,df):
        plt.subplot(2, 1, 1)
        fig, ax = plt.subplots()
        df.groupby(feat).Survived.value_counts().plot(kind="bar")
        plt.figure(figsize=(12,8))
        plt.subplot(2, 1, 2)
        sns.barplot(x=feat, y="Survived", data=df)
        plt.show()
        st.pyplot(fig)

    def histograma(self,df):
        fig, ax = plt.subplots()
        ax.hist(df, bins=20)

        st.pyplot(fig)


    def ErrorValoresNumerico(self,cadena1,cadena2):
      
        if cadena1=="Embarked" and cadena2=="Sex":
            return False
            
        if cadena2=="Embarked" and cadena1=="Sex":
            return False
        return True


    def iniciaGraficios(self,lista,df,existeEmbarke):
        st.write("")

        col1, col2 = st.columns(2)
        with col1:
            datos = st.radio(
            "Elegir graficos",
            ('No Aplicar','histograma', 'Grafica Barra','Violint'))
        
       
        with col2:
            if datos=='histograma':
                nuevalista=lista
        
                if(existeEmbarke):
                    nuevalista.remove("Embarked")
            

                elegirhis = st.selectbox(
                "Elegir filtro",
                nuevalista)
            
                self.histrogama(df[elegirhis])

            if datos=='Grafica Barra':

                elegirBar = st.selectbox(
                "Elegir filtro",
                lista)
                
                self.funcion_graficas(elegirBar,df)
                

            if datos=='Violint':
            
                elegirval = st.selectbox(
                "Elegir valor",
                lista,key="dos")
                if elegirval !="":
                    elegirva2 = st.selectbox(
                    "Elegir valor",
                    lista,key="uno")
                    if elegirval!=elegirva2 and self.ErrorValoresNumerico(elegirval,elegirva2):
                        self.violinplot(elegirval,elegirva2,"Survived",df)
                    elif elegirval==elegirva2:
                        st.write("Para  dibujar este Gráfico los dos valores debe ser distintos")
                    else:
                         st.write("Para  dibujar este Gráfico al menos un valor debe ser númerico")

            if datos=="No Aplicar":
                st.write("")
        
