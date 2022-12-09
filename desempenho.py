import streamlit as st

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
    A seguir teremos uma análise exploratória dos dados referentes uma pesquisa sobre notas e algumas características de alunos do primeiro, segundo e terceiro ano de 2 escolas portuguesas.
    
    ### Dataset Columns
    """)
    st.markdown("""
    1. school - Escola (binary: 'GP' - Gabriel Pereira ou 'MS' - Mousinho da Silveira)
    2. sex - sexo (binary: 'F' - feminino ou 'M' - masculino)
    3. age - idade (numeric: de 15 a 22)
    4. address - tipo de endereço (binary: 'U' - urbano ou 'R' - rural)
    5. famsize - tamanho da família (binary: 'LE3' - menor ou igual a 3 ou 'GT3' - maior que 3)
    6. Pstatus - status dos pais (binary: 'T' - morando juntos ou 'A' - separados)
    7. Medu - educação da mãe (numeric: 0 - nenhuma, 1 - educação primária (até quarta série), 2 - quinto ao nono ano, 3 - ensino médio ou 4 - ensino superior)
    8. Fedu - educação do pai (numeric: 0 - nenhuma, 1 - educação primária (até quarta série), 2 - quinto ao nono ano, 3 - ensino médio ou 4 - ensino superior)
    9. Mjob - trabalho da mãe (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
    10. Fjob - trabalho do pai (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
    11. reason - razão por escolher a escola (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
    12. guardian - student's guardian (nominal: 'mother', 'father' or 'other')
    13. traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
    14. studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
    15. failures - number of past class failures (numeric: n if 1<=n<3, else 4)
    16. schoolsup - extra educational support (binary: yes or no)
    17. famsup - family educational support (binary: yes or no)
    18. paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
    19. activities - extra-curricular activities (binary: yes or no)
    20. nursery - attended nursery school (binary: yes or no)
    21. higher - wants to take higher education (binary: yes or no)
    22. internet - Internet access at home (binary: yes or no)
    23. romantic - with a romantic relationship (binary: yes or no)
    24. famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
    25. freetime - free time after school (numeric: from 1 - very low to 5 - very high)
    26. goout - going out with friends (numeric: from 1 - very low to 5 - very high)
    27. Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
    28. Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
    29. health - current health status (numeric: from 1 - very bad to 5 - very good)
    30. absences - number of school absences (numeric: from 0 to 93)
    these grades are related with the course subject, Math or Portuguese:
    31. G1 - first period grade (numeric: from 0 to 20)
    32. G2 - second period grade (numeric: from 0 to 20)
    33. G3 - final grade (numeric: from 0 to 20, output target)
    """)