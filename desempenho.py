import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

with st.expander('Cabeçalho'):
    st.title('Programa Diversidade Tech')
    st.title('ADA + Suzano')
    st.markdown("""
        # Disciplina: Técnicas de Programação II
        ## Professor: Leonardo Borges:sports_medal:
        Alunos:   
        **Cíntia Dantas**\n
        **Júlia Cavalcante**\n
        **Júnior Aguiar**\n
        **Rafael Bittencourt**
    """)
with st.expander('Introdução'):
    st.title('Análise Exploratória')
    st.markdown("""
    A seguir teremos uma análise exploratória dos dados referentes uma pesquisa sobre 
    
    ### Dataset Columns
    """)
    st.markdown("""
    1. gender - Gênero (booleana: 'female' ou 'male')
    2. race/ethnicity - raça/etnia (nominal: 5 grupos 'group A', 'group B' etc.)
    3. parental level of education - nível educacional dos responsáveis (nominal: 'some college', '')
    4.
    """)
    
# função que carrega o dataset
def carregar_dataset(nome_dataset):
    return pd.read_csv(nome_dataset)

st.header('Dataset')
nome_dataset = st.text_input('Qual o nome do dataset que deseja carregar?',
                             value='desempenho')

if nome_dataset:
    df = carregar_dataset('StudentsPerformance.csv')

# SIDEBAR
## SIDEBAR - Filtro dos campos
with st.sidebar:
    st.title('Filtros')
    cols_selected = \
        st.multiselect('Filtre os campos que deseja analisar:',
                       options=list(df.columns),
                       default=list(df.columns))
    frac_sample = \
        st.slider('Defina o percentual do dataset para análise:', 
                  min_value=1, max_value=100, value=50, step=1)

df_selected = df[cols_selected].sample(frac=frac_sample/100)

## CORPO - Info do dataset
with st.expander('Dados do Dataset'):
    st.header('Dados do Dataset')
    st.subheader('Primeiros registros')
    st.write(df_selected.head())
    
    st.subheader('Colunas')
    for col in df_selected.columns:
        st.text(f'- {col}')
        
    st.subheader('Dados Faltantes')
    st.write(df_selected.isna().sum()[df_selected.isna().sum() > 0])

    st.subheader('Estatísticas Descritivas')
    st.write(df_selected.describe())

## CORPO - Análise Univariada
st.header('Análise Univariada')
univar_campo =  \
    st.selectbox('Selecione o campo que deseja avaliar a distribuição:',
                 options=list(df_selected.select_dtypes(include=np.number)))


st.plotly_chart(px.histogram(data_frame=df_selected, x=univar_campo))
st.plotly_chart(px.box(data_frame=df_selected, y=univar_campo))

## CORPO - Análise Bivariada
st.header('Análise Bivariada')
bivar_graf_option = \
    st.radio('Escolha um tipo de gráfico:',
             options=['dispersão', 'boxplot', 'pairplot'])

### CORPO - Análise Bivariada - gráfico de dispersão
if bivar_graf_option == 'dispersão':
    campo_dispersao_1 =  \
        st.selectbox('Selecione primeira variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    campo_dispersao_2 =  \
        st.selectbox('Selecione segunda variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    st.plotly_chart(
        px.scatter(data_frame=df_selected, 
                   x=campo_dispersao_1, 
                   y=campo_dispersao_2)
    )

### CORPO - Análise Bivariada - gráfico de boxplot       
elif bivar_graf_option == 'boxplot':
    campo_boxplot_num =  \
        st.selectbox('Selecione uma variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    campo_boxplot_cat =  \
        st.selectbox('Selecione uma variável categórica:',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
        
    st.plotly_chart(
        px.box(data_frame=df_selected, 
                   x=campo_boxplot_cat, 
                   y=campo_boxplot_num)
    )

### CORPO - Análise Bivariada - gráfico de pairplot  
else:
    pairplot = sns.pairplot(df_selected)
    st.pyplot(pairplot)

## CORPO - Análise Multivariada
st.header('Análise Multivariada')
multivar_graf_option = \
    st.radio('Escolha um tipo de gráfico:',
             key='multivar_graf_option',
             options=['dispersão', 'boxplot', 'pairplot'])

if multivar_graf_option == 'dispersão':
    multivar_dispersao_num1 =  \
        st.selectbox('Selecione primeira variável numérica:',
                     key='multivar_dispersao_num1',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    multivar_dispersao_num2 =  \
        st.selectbox('Selecione segunda variável numérica:',
                     key='multivar_dispersao_num2',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    multivar_dispersao_seg = \
        st.selectbox('Selecione uma variável categórica para segmentar:',
                     key='multivar_dispersao_seg',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
    
    multivar_dispersao_check = \
        st.checkbox('Adicionar linha de tendência')
    
    if multivar_dispersao_check:
        st.plotly_chart(
            px.scatter(data_frame=df_selected, 
                    x=multivar_dispersao_num1, 
                    y=multivar_dispersao_num2,
                    color=multivar_dispersao_seg,
                    trendline='ols')
        )
    else:
        st.plotly_chart(
            px.scatter(data_frame=df_selected, 
                    x=multivar_dispersao_num1, 
                    y=multivar_dispersao_num2,
                    color=multivar_dispersao_seg)
        )
        
elif multivar_graf_option == 'boxplot':
    multivar_boxplot_num =  \
        st.selectbox('Selecione uma variável numérica:',
                     key='multivar_boxplot_num',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    multivar_boxplot_cat =  \
        st.selectbox('Selecione uma variável categórica:',
                     key='multivar_boxplot_cat',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
        
    multivar_boxplot_seg =  \
        st.selectbox('Selecione uma variável categórica para segmentar:',
                     key='multivar_boxplot_seg',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
        
    st.plotly_chart(
        px.box(data_frame=df_selected, 
                   x=multivar_boxplot_cat, 
                   y=multivar_boxplot_num,
                   color=multivar_boxplot_seg)
    )
    
else:
    multivar_pairplot_seg =  \
        st.selectbox('Selecione uma variável categórica:',
                     key='multivar_pairplot_seg',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
        
    multivar_pairplot = sns.pairplot(df_selected, hue=multivar_pairplot_seg)
    st.pyplot(multivar_pairplot)   