import plotly.express as px

# Criar um gráfico interativo
fig = px.bar(df, x='Mês', y='Gasto', title='Gastos Totais por Mês')
fig.show()
