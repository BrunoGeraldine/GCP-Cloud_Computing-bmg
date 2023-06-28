import pandas as pd
import numpy as np
import streamlit as st
from datetime import date
from plotly   import graph_objects as go

#Configurando a aparência do Gráfico default
st.set_page_config(page_title='Análise de Multas PRF - 2022',
                   page_icon= '🧊',
                   layout= 'wide')

# Supress Scientific Notation
np.set_printoptions(suppress=True)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

st.header('Análise das multas emitidas pela PRF - 2022')

st.text('Este projeto visa demonstrar o potencial de visualização da análise de dados, utilizando o Streamlit')

#criando a side bar
st.sidebar.header('Escolha a UF do estado')

#Coletando o nome e sigla da ação escolhida
@st.cache_data
def pegar_dados_uf():
    path = '../dataset/uf_valor_total.parquet'
    return pd.read_parquet(path)

df = pegar_dados_uf()

#Coletando o nome e sigla da ação escolhida
@st.cache_data
def pegar_valores_uf():
    path = '../dataset/uf_valor_total.parquet'
    return pd.read_parquet(path)

df1 = pegar_valores_uf()



uf = df['UF Infração']
uf_escolhido = st.sidebar.selectbox('Escolha uma UF', uf)


st.subheader('Tabela de Valores - ' + uf_escolhido)
st.write(df1.tail(28).sort_values(by='Qtdd', ascending=False))


#Criando grafico
st.subheader('Grafico de Multas')
fig = go.Figure()
fig.add_trace(go.Scatter(x=df1['UF Infração'],
                         y=df1['Qtdd'],
                         name='Quantidade de Multas po Estado',
                         line_color='gray'))


fig.add_trace(go.Scatter(x=df1['UF Infração'],
                         y=df1['Total'],
                         name='Total de Multas po Estado',
                         line_color='orange'))

fig.update_layout(width=1400, height=500, font_size=12, dragmode='zoom')

st.plotly_chart(fig)