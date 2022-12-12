import pandas as pd

# função que carrega o dataset
def carregar_dataset() -> pd.DataFrame:
    return pd.read_csv('https://raw.githubusercontent.com/Rabittencourt/desempenho_escolar/main/StudentsPerformance.csv')