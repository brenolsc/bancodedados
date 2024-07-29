import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo dos gráficos
sns.set(style="whitegrid")

# Gráfico de Gastos por Mês
plt.figure(figsize=(10, 6))
sns.barplot(x=gastos_por_mes.index.astype(str), y=gastos_por_mes.values, palette="Blues_d")
plt.title('Gastos Totais por Mês')
plt.xlabel('Mês')
plt.ylabel('Gasto Total')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de Avaliações
plt.figure(figsize=(8, 5))
sns.histplot(df['Avaliação'], bins=5, kde=True, color='purple')
plt.title('Distribuição das Avaliações')
plt.xlabel('Avaliação')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()
