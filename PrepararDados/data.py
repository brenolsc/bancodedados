import pandas as pd
import numpy as np

# Gerar dados
data = {
    'Cliente': ['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D', 'Cliente E'],
    'Data_Evento': ['2024-01-15', '2024-01-20', '2024-01-25', '2024-02-01', '2024-02-10'],
    'Gasto': [500, 700, 300, 400, 600],
    'Avaliação': [4, 5, 3, 4, 5]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Converter a coluna 'Data_Evento' para datetime
df['Data_Evento'] = pd.to_datetime(df['Data_Evento'])

# Exibir as primeiras linhas do DataFrame
print(df.head())

