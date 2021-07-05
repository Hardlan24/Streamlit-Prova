#!/usr/bin/env python
# coding: utf-8

# ## Generarem Pagina Web Interactiva

# #### Instalem llibreries

# In[1]:


import streamlit as st
from PIL import Image
import pandas as pd
import requests
import json


# #### Capçalera

# In[2]:


image = Image.open('Logo batalle.jpg')

st.image(image, width = 200)

st.title('Anàlisi Projecte X Batallé')
st.markdown("""
Aquest estudi analitza el projecte X
""")


# #### Barra lateral i Panell Principal

# In[3]:


#Barra lateral
st.sidebar.header('Opcions Entrada')

## barra lateral opcions
#currency_list
opcions = ['Economic', 'Avantatges i Inconvenients', 'Impacte Ambiental', 'Cronograma','Posta a Punt']
#base_price_unit 
seleccio = st.sidebar.selectbox('Selecciona la opció que vulguis observar', opcions)


# #### Generem base de dades de Prova

# In[4]:


import numpy as np
X=np.random.rand(100,5)
columns=np.arange(0,5,1)


# In[5]:


df=pd.DataFrame(X,columns=columns)
df.head()


# #### Generem Funcions per a cada Opció

# In[6]:


import plotly.express as px
def economic(df):
    st.header('Anàlisi Econòmic')
    st.markdown("""S'observa l'anàlisi Econòmic scatter plot entre columnes 0 i 1 """)
    fig = px.scatter(x=df[0], y=df[1])
    st.plotly_chart(fig)
def avantinc(df):
    st.header('Avantatges i Inconvenients')
    st.markdown("""S'observen els avantages i inconvenients bar plot entre columnes 0 i 1 """)
    fig = px.bar(x=df[0], y=df[1])
    st.plotly_chart(fig)
def ambient(df):
    st.header('Impacte Ambiental')
    st.markdown("""S'observa l'impacte ambiental scatter entre columnes 2 i 3 """)
    fig = px.scatter(x=df[2], y=df[3])
    st.plotly_chart(fig)
def crono(df):
    st.header('Cronograma')
    st.markdown("""S'observa el cronogramascatter entre columnes 0 i 3 """)
    fig = px.scatter(x=df[0], y=df[3])
    st.plotly_chart(fig)
def papunt(df):
    st.header('Posta a Punt')
    st.markdown("""S'observa la posta a punt scatter entre columnes 1 i 3 """)
    fig = px.scatter(x=df[1], y=df[3])
    st.plotly_chart(fig)
    
    
    


# In[7]:


if seleccio == 'Economic':
    economic(df)
elif seleccio == 'Avantatges i Inconvenients':
    avantinc(df)  
elif seleccio == 'Impacte Ambiental':
    ambient(df)
elif seleccio == 'Cronograma':
    crono(df)
if seleccio == 'Posta a Punt':
    papunt(df)


# In[ ]:





# In[ ]:




