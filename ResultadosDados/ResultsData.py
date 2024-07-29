# Salvar o DataFrame atualizado em um arquivo CSV
df.to_csv('dados_clientes.csv', index=False)

# Exportar gráficos
plt.figure(figsize=(10, 6))
sns.barplot(x=gastos_por_mes.index.astype(str), y=gastos_por_mes.values, palette="Blues_d")
plt.title('Gastos Totais por Mês')
plt.xlabel('Mês')
plt.ylabel('Gasto Total')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('gastos_por_mes.png')

plt.figure(figsize=(8, 5))
sns.histplot(df['Avaliação'], bins=5, kde=True, color='purple')
plt.title('Distribuição das Avaliações')
plt.xlabel('Avaliação')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('distribuicao_avaliacoes.png')
