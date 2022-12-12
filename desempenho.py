import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from funcoes import carregar_dataset

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
    st.title('Análise Exploratória de desempenho estudantil')
    
    ## Introdução: contém o objetivo/propósito da análise
    st.markdown("""
            #### Trata-se de trabalho de conclusão do módulo IV - Técnicas de programação II, ministrado por Leonardo Borges.
            #### O objetivo desta análise é investigar se existe relação entre as notas dos alunos e outras duas variáveis: o grau de escolaridade dos seus pais e a conclusão de curso preparatório para o teste
            ---
            """) 
    st.markdown("""
    ### Colunas do Dataset
    1. gender - Gênero: (booleana: 'female' ou 'male')
    2. race/ethnicity - raça/etnia: (nominal: 5 grupos 'group A', 'group B' etc.)
    3. parental level of education - nível educacional dos responsáveis: (nominal: 'some college', '')
    4. lunch - Almoço (ou refeição): (nominal: 'standard' e 'free/reduced' ) 
    5. test preparation course - curso preparatório para testes (nominal: 'none' e 'completed')
    6. math score - Nota em matemática (inteiro: 0 a 100)
    7. reading score - Nota em leitura (inteiro: 0 a 100)
    8. writing score - Nota em escrita (inteiro: 0 a 100)
    """)
    
    ## Descrição dos Dados: descrição inicial dos dados
    st.markdown("""
            #### O dataset contém registros sobre alunos, incluindo dados pessoais, sociais, econômicos e escolares de três exames realizados, das disciplinas de matemática, leitura e escrita.
            ##### Link do dataset: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
            ---
            """)
    
st.header('Dataset')
nome_dataset = st.text_input('Qual o nome do dataset que deseja carregar?',
                             value='desempenho')

if nome_dataset:
    df = carregar_dataset()

# SIDEBAR - Filtro de colunas
with st.sidebar:
    st.title('Filtros')
    cols_selected = \
        st.multiselect('Filtre os campos que deseja analisar:',
                       options=list(df.columns),
                       default=list(df.columns))

df_selected = df[cols_selected]

## SIDEBAR - Filtro de amostra
with st.sidebar:
    st.title('Amostra')
    amostra = \
        st.slider('Selecione a porcentagem da amostra desejada:', 
                  min_value=1, max_value=100, step=1)
    amostra = amostra/100
    df_selected = df_selected.sample(frac = amostra)


## CORPO - Informações gerais do dataset
with st.expander('Dados gerais do dataset'):
    st.subheader('Primeiros registros')
    st.write(df_selected.head())
    
    st.subheader('Tamanho do Dataset')
    st.write('Quantidade de linhas:', df_selected.shape[0])
    st.write('Quantidade de colunas:', df_selected.shape[1])
    
    if st.checkbox('Exibir dados das colunas'):
        st.markdown("""
            - gender: feminino (female) ou masculino (male)
            - race/ethnicity: grupo A, grupo B, grupo C, grupo D e grupo E
            - parental level of education: escolaridade dos pais
            - lunch: almoço padrão (standard) ou grátis/reduzido ('free/reduced')
            - test preparation course: curso de preparação para o teste
            - math score: nota do teste de matemática
            - reading score: nota do teste de leitura
            - writing score: nota do teste de escrita
            """)

    st.subheader('Dados Faltantes')
    st.write(df_selected.isna().sum()[df_selected.isna().sum() > 0])

    st.subheader('Estatísticas Descritivas')
    st.write(df_selected.describe())


## CORPO - Análise Univariada
# Variáveis numéricas
st.header('Análise Univariada')
st.subheader('Distribuição das variáveis numéricas')
univar_campo_num =  \
    st.selectbox('Selecione o campo cuja distribuição você deseja avaliar:',
                 options=list(df_selected.select_dtypes(include=np.number)))

st.write('Histograma')
st.plotly_chart(px.histogram(
    data_frame=df_selected, 
    x=univar_campo_num, 
    text_auto=True,
    color_discrete_sequence=px.colors.qualitative.Set2))
    
st.write('Gráfico de caixa')
st.plotly_chart(px.box(data_frame=df_selected, y=univar_campo_num, color_discrete_sequence=px.colors.qualitative.Vivid))

# Variáveis categóricas
st.subheader('Participação das variáveis categóricas')
univar_campo_cat =  \
    st.selectbox('Selecione o campo cuja distribuição você deseja avaliar:',
                 options=list(df_selected.select_dtypes(exclude=np.number)))

st.write('Gráfico de pizza')
contagem = df[univar_campo_cat].value_counts().values
var_cat = df[univar_campo_cat].value_counts().index

fig1, ax1 = plt.subplots(figsize = (5,3))
ax1.pie(contagem, labels=var_cat, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

st.markdown("""
            #### Análise da seção:
            ##### A média das notas de matemática, de leitura e de escrita é muito parecida.
            ##### Quanto ao nível de educação dos pais, a maioria deles possui associate’s degree (semelhante à graduação de tecnólogo no Brasil) e frequentou a graduação, sem obter o título.
            ##### Quanto ao curso pré-teste, a maioria dos alunos não fez o curso preparativo para o teste.""")


## CORPO - Análise Bivariada
st.header('Análise Bivariada')
bivar_graf_option = \
    st.radio('Escolha um tipo de gráfico:',
             options=['Barras', 'Dispersão', 'Boxplot', 'Boxenplot', 'Pairplot'],
             key='bivar_graF_option')

# Barras
if bivar_graf_option == 'Barras':
    bivar_barras_cat =  \
        st.selectbox('Selecione uma variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    bivar_barras_num =  \
        st.selectbox('Selecione uma variável categórica:',
                     options=list(df_selected.select_dtypes(exclude=np.number)))

    st.plotly_chart(px.histogram(
        data_frame=df_selected, 
        y=bivar_barras_cat, 
        x=bivar_barras_num,
        histfunc='avg',
        text_auto='.2f',
        category_orders={'parental level of education': ['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree','master\'s degree'],
                         'race/ethnicity': ['group A', 'group B', 'group C', 'group D', 'group E'],
                         'test preparation course': ['none', 'completed']},
        color_discrete_sequence=px.colors.qualitative.Pastel1))

## Dispersão
elif bivar_graf_option == 'Dispersão':
    bivar_dispersao_num1 =  \
        st.selectbox('Selecione a primeira variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    bivar_dispersao_num2 =  \
        st.selectbox('Selecione a segunda variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))

    if st.checkbox('Exibir linha de tendência'):
        st.plotly_chart(
            px.scatter(data_frame=df_selected, 
                    x=bivar_dispersao_num1, 
                    y=bivar_dispersao_num2,
                    trendline='ols',
                    trendline_color_override="red",
                    color_discrete_sequence=px.colors.qualitative.Antique))
    else:
        st.plotly_chart(
        px.scatter(data_frame=df_selected, 
                   x=bivar_dispersao_num1, 
                   y=bivar_dispersao_num2,
                   color_discrete_sequence=px.colors.qualitative.Antique)
    )

## Boxplot        
elif bivar_graf_option == 'Boxplot':
    bivar_boxplot_num =  \
        st.selectbox('Selecione uma variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    bivar_boxplot_cat =  \
        st.selectbox('Selecione uma variável categórica:',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
        
    st.plotly_chart(
        px.box(data_frame=df_selected, 
                   x=bivar_boxplot_cat, 
                   y=bivar_boxplot_num,
                   category_orders={'parental level of education': ['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree','master\'s degree'],
                                    'race/ethnicity': ['group A', 'group B', 'group C', 'group D', 'group E'],
                                    'test preparation course': ['none', 'completed']})
    )

# Boxenplot    
elif bivar_graf_option == 'Boxenplot':
    bivar_boxenplot_num =  \
        st.selectbox('Selecione uma variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)))
        
    bivar_boxenplot_cat =  \
        st.selectbox('Selecione uma variável categórica:',
                     options=list(df_selected.select_dtypes(exclude=np.number)))
    
    fig2, ax2 = plt.subplots(figsize=(13,5))

    if bivar_boxenplot_cat == 'parental level of education':
        sns.boxenplot(data=df_selected, 
                        x=bivar_boxenplot_cat, 
                        y=bivar_boxenplot_num,
                        order=['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree', 'master\'s degree'])

    elif bivar_boxenplot_cat == 'race/ethnicity':
        sns.boxenplot(data=df_selected, 
                        x=bivar_boxenplot_cat, 
                        y=bivar_boxenplot_num,
                        order=['group A', 'group B', 'group C', 'group D', 'group E'])

    elif bivar_boxenplot_cat == 'test preparation course':
        sns.boxenplot(data=df_selected, 
                        x=bivar_boxenplot_cat, 
                        y=bivar_boxenplot_num,
                        order=['none', 'completed'])

    else:
        sns.boxenplot(data=df_selected, 
                        x=bivar_boxenplot_cat, 
                        y=bivar_boxenplot_num)
   
    st.pyplot(fig2)

#Pairplot
else:
    bivar_pairplot = sns.pairplot(df_selected)
    st.pyplot(bivar_pairplot, key='bivar_pairplot')

st.markdown("""
            #### Análise da seção:
            ##### Conforme o gráfico de barras, os alunos cujos pais possuem maior nível educacional obtêm notas discretamente maiores, sobretudo nos testes de matemática e leitura. Essa informação é confirmada pelos gráficos de caixas, que mostram distribuições com valores mais altos conforme aumenta o nível de educação.
            ##### Também pelo gráfico de barras, os alunos que fizeram o curso possuem média de notas inferiores para leitura e escrita, comparados aos que não o fizeram. Observando os gráficos de caixas, temos que a média não é uma medida ideal, pois claramente as distribuições mostram que a maioria dos alunos que fizeram o curso tiveram notas mais altas, sobretudo para as provas de leitura e escrita.
            ##### Pelo gráfico de dispersão, existe correlação positiva entre as notas, evidenciada pela linha de tendência, logo, quanto maior é a nota em uma disciplina, maior é a da outra.""")


## CORPO - Análise Multivariada
st.header('Análise Multivariada')
multivar_graf_option = \
    st.radio('Escolha um tipo de gráfico:',
             options=['Barras', 'Dispersão', 'Boxplot', 'Violino', 'Pairplot'],
             key='multivar_graf_option')

# Barras
if multivar_graf_option == 'Barras':
    multivar_barras_num =  \
        st.selectbox('Selecione uma variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)),
                     key='multivar_barras_num')
        
    multivar_barras_cat =  \
        st.selectbox('Selecione uma variável categórica:',
                     options=list(df_selected.select_dtypes(exclude=np.number)),
                     key='multivar_barras_cat')

    multivar_barras_seg =  \
        st.selectbox('Selecione uma variável categórica para segmentação:',
                     options=list(df_selected.select_dtypes(exclude=np.number)),
                     key='multivar_barras_seg')
    
    fig3 = st.plotly_chart(px.histogram(data_frame=df_selected, 
                                        x=multivar_barras_cat, 
                                        y=multivar_barras_num,
                                        color=multivar_barras_seg,
                                        barmode='group',
                                        histfunc='avg',
                                        text_auto='.2f',
                                        category_orders={'parental level of education': ['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree','master\'s degree'],
                                                         'race/ethnicity': ['group A', 'group B', 'group C', 'group D', 'group E'],
                                                         'test preparation course': ['none', 'completed']},
                                        color_discrete_sequence=px.colors.qualitative.Pastel1))

# Dispersão
elif multivar_graf_option == 'Dispersão':
    multivar_campo_dispersao_1 =  \
        st.selectbox('Selecione primeira variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)),
                     key = 'dispersao1_multivar')
        
    multivar_campo_dispersao_2 =  \
        st.selectbox('Selecione segunda variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)),
                     key = 'dispersao2_multivar')
        
    multivar_campo_dispersao_3 =  \
        st.selectbox('Selecione uma variável categórica para segmentação:',
                     options=list(df_selected.select_dtypes(exclude=np.number)),
                     key = 'dispersao3_multivar')

    multivar_campo_dispersao_4 = \
        st.checkbox('Adicionar linha de tendência',
                    key = 'dispersao4_multivar')

    if multivar_campo_dispersao_4:
        st.plotly_chart( 
            px.scatter(data_frame=df_selected, 
                    x=multivar_campo_dispersao_1, 
                    y=multivar_campo_dispersao_2,
                    color=multivar_campo_dispersao_3,
                    trendline='ols',
                    color_discrete_sequence=px.colors.qualitative.Set1))

    else:
        st.plotly_chart( 
            px.scatter(data_frame=df_selected, 
                    x=multivar_campo_dispersao_1, 
                    y=multivar_campo_dispersao_2,
                    color=multivar_campo_dispersao_3,
                    color_discrete_sequence=px.colors.qualitative.Set1)
    )

# Boxplot       
elif multivar_graf_option == 'Boxplot':
    multivar_campo_boxplot_num =  \
        st.selectbox('Selecione uma variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)),
                     key = 'boxplot1_multivar')
        
    multivar_campo_boxplot_cat =  \
        st.selectbox('Selecione uma variável categórica:',
                     options=list(df_selected.select_dtypes(exclude=np.number)),
                     key = 'boxplot2_multivar')
        
    multivar_campo_boxplot_seg =  \
        st.selectbox('Selecione uma variável categórica para segmentação:',
                     options=list(df_selected.select_dtypes(exclude=np.number)),
                     key = 'boxplot3_multivar')

    st.plotly_chart(
        px.box(data_frame=df_selected, 
                x=multivar_campo_boxplot_cat, 
                y=multivar_campo_boxplot_num,
                color=multivar_campo_boxplot_seg,
                category_orders={'parental level of education': ['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree','master\'s degree'],
                                'race/ethnicity': ['group A', 'group B', 'group C', 'group D', 'group E'],
                                'test preparation course': ['none', 'completed']})
    )

# Violino       
elif multivar_graf_option == 'Violino':
    multivar_campo_violin_num =  \
        st.selectbox('Selecione uma variável numérica:',
                     options=list(df_selected.select_dtypes(include=np.number)),
                     key = 'violin1_multivar')
        
    multivar_campo_violin_cat =  \
        st.selectbox('Selecione uma variável categórica:',
                     options=list(df_selected.select_dtypes(exclude=np.number)),
                     key = 'violin2_multivar')
        
    multivar_campo_violin_seg =  \
        st.selectbox('Selecione uma variável categórica para segmentação:',
                     options=list(df_selected.select_dtypes(exclude=np.number)),
                     key = 'violin3_multivar')

    fig3, ax3 = plt.subplots(figsize=(13,5))
    if multivar_campo_violin_cat == 'race/ethnicity':
            sns.violinplot(data=df_selected, 
                   x=multivar_campo_violin_cat, 
                   y=multivar_campo_violin_num,
                   hue=multivar_campo_violin_seg,
                   order=['group A', 'group B', 'group C', 'group D', 'group E'])

    elif multivar_campo_violin_cat == 'parental level of education':
            sns.violinplot(data=df_selected, 
                   x=multivar_campo_violin_cat, 
                   y=multivar_campo_violin_num,
                   hue=multivar_campo_violin_seg,
                   order=['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree', 'master\'s degree'])    
    
    elif multivar_campo_violin_cat == 'test preparation course':
            sns.violinplot(data=df_selected, 
                   x=multivar_campo_violin_cat, 
                   y=multivar_campo_violin_num,
                   hue=multivar_campo_violin_seg,
                   order=['none', 'completed'])    

    else:
        sns.violinplot(data=df_selected, 
                   x=multivar_campo_violin_cat, 
                   y=multivar_campo_violin_num,
                   hue=multivar_campo_violin_seg)

    ax3.set_xlabel(multivar_campo_violin_cat, fontsize=20)
    ax3.set_ylabel(multivar_campo_violin_num, fontsize=20)
    ax3.tick_params(labelsize=13)
    sns.move_legend(ax3, "upper left", bbox_to_anchor=(1, 1))
    plt.setp(ax3.get_legend().get_texts(), fontsize='20') 
    plt.setp(ax3.get_legend().get_title(), fontsize='20') 
    st.pyplot(fig3)

# Pairplot  
else:
    multivar_campo_pairplot_seg =  \
        st.selectbox('Selecione uma variável categórica para segmentação:',
                     options=list(df_selected.select_dtypes(exclude=np.number)))

    multivar_pairplot = sns.pairplot(df_selected, hue = multivar_campo_pairplot_seg)
    st.pyplot(multivar_pairplot, key='multivar_pairplot')

st.markdown("""
            #### Análise da seção:
            ##### Pelo gráfico de barras, vemos que a média dos alunos que fizeram o curso preparatório é maior dos que não fizeram, independente do grau de instrução dos pais. Entretanto, de forma geral, a média é maior quanto maior for o nível de instrução.
            ##### O mesmo é observado com os gráficos de caixas das notas por nível de educação, segmentado pela variável curso.
            ##### O gráfico de dispersão segmentado pela variável curso evidencia que a correlação é mais forte quando o aluno fez o curso, de modo que as notas das disciplinas são maiores para eles.""")

st.markdown("""
            #### Conclusão:
            ##### A conclusão do curso preparatório para os testes influencia positivamente nas notas dos alunos.
            ##### O maior nível de escolaridade dos pais também é positiva, mas em menor intensidade.
            ##### Por falta de informações sobre as colunas de etnia optamos por não analisá-las. 
            ##### Percebemos que as variações das notas devido ao gênero ou tipo de refeição não eram tão grandes e portanto optamos, também, por não incluir tais análises.""")   