# Análise Descritiva
print(df.describe())

# Análise de Média de Gastos por Mês
df['Mês'] = df['Data_Evento'].dt.to_period('M')
gastos_por_mes = df.groupby('Mês')['Gasto'].sum()
print("Gastos por Mês:")
print(gastos_por_mes)

# Média de Avaliações
media_avaliacoes = df['Avaliação'].mean()
print(f"Média das Avaliações: {media_avaliacoes:.2f}")

