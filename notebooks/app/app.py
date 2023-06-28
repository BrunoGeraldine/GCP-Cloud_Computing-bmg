import numpy          as np
import pandas         as pd
import streamlit      as st
import plotly.express as px

from PIL      import Image
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

#Coleta dos dados
@st.cache_data
def pegar_dados_uf():
    path = '../dataset/uf_valor_total.parquet'
    return pd.read_parquet(path)

df = pegar_dados_uf()

@st.cache_data
def pegar_valores_uf():
    path = '../dataset/uf_valor_total.parquet'
    return pd.read_parquet(path)

df1 = pegar_valores_uf()

@st.cache_data
def pegar_valores_mes():
    path = '../dataset/anl_mes.parquet'
    return pd.read_parquet(path)

df_mes = pegar_valores_mes()


#criando a side bar

uf = df1['UF Infração']
sigla_uf_escolhida = st.sidebar.selectbox('Escolha a UF do estado', uf)

df_uf = df1[df1['UF Infração'] == sigla_uf_escolhida]
uf_escolhida = df_uf.iloc[0]['UF Infração']
#
#
#
#image = Image.open('logopf.webp')
#st.image(image)
#
st.subheader('Tabela de Valores')
st.write(df1.tail(28).sort_values(by='Qtdd', ascending=False))

#
##Criando grafico
#st.subheader('Grafico - Valor Total Multas')
#fig = go.Figure()
#fig.add_trace(go.Bar(x=df1['UF Infração'],
#                     y=df1['Total'],
#                     name='Total em Multas po Estado'))
#
#fig.update_layout(width=1400, height=500, font_size=12, dragmode='zoom')
#
#st.plotly_chart(fig)
#
#Criando grafico
st.subheader('Grafico - Valor Total Multas P/ Mês')
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df_mes['Mês'],
                         y=df_mes['Total_mes'],
                         name='Quantidade de Multas po Estado',
                         line_color='orange'))

fig2.update_layout(width=1400, height=500, font_size=12, dragmode='zoom')

st.plotly_chart(fig2)


#fig2 = px.line(x=df_mes['Mês'], y=df_mes['Total_mes'])
##fig2.write_html('first_figure.html', auto_open=True)
#st.plotly_chart(fig2)