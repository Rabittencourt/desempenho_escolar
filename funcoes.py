import pandas as pd

# função que carrega o dataset
def carrega_dataset() -> pd.DataFrame:
    return pd.read_csv('https://raw.githubusercontent.com/cintiadantas20/modulo-IV-diversidade_tech-turma-892/main/Desafio/StudentsPerformance.csv')