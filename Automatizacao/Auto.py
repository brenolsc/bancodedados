import pandas as pd
from sqlalchemy import create_engine

# automação de ETL
def extract_data():
    # Simulação da extração de dados de um banco de dados
    engine = create_engine('sqlite:///theotokos.db') 
    query = 'SELECT * FROM eventos'
    df = pd.read_sql(query, engine)
    return df

def transform_data(df):
    # Limpeza e transformação dos dados
    df['Data_Evento'] = pd.to_datetime(df['Data_Evento'])
    return df

def load_data(df):
    # Salvando dados transformados em um novo banco de dados ou arquivo
    df.to_csv('dados_transformados.csv', index=False)

df = extract_data()
df = transform_data(df)
load_data(df)
