import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os
os.system('cls')

# Usando outra database
outro_filmes = pd.read_csv('./dados/tmdb_movies.csv', delimiter=',')
#print(outro_filmes.head())
#print(outro_filmes.original_language.unique())
qtde_linguas = outro_filmes.original_language.value_counts().to_frame().reset_index()
qtde_linguas.columns = ['original_language', 'total']
#print('Frequencia das linguas \n',qtde_linguas)

# mesmo resultado, grafico de barras
#sns.barplot(x = 'original_language', y = 'total', data = qtde_linguas)
#sns.catplot(x = 'original_language', kind='count', data = outro_filmes)

# grafico de pizza
#plt.pie(qtde_linguas['total'], labels=qtde_linguas['original_language'])

# grafico de comparação 
todos = outro_filmes.original_language.value_counts()
total_geral = todos.sum()
total_ingles = todos.loc['en']
total_resto = total_geral - total_ingles
dados = {
  'lingua':['ingles','outros'],
  'total':[total_ingles, total_resto]
}
dados = pd.DataFrame(dados)
# sns.barplot(x='lingua', y='total', data=dados)
# plt.pie(dados.total, labels=dados.lingua)
# plt.show()

# buscando o que nao eh ingles
nao_ingles = outro_filmes.query("original_language != 'en'")
indice = outro_filmes.query("original_language != 'en'").original_language.value_counts()
#print(nao_ingles)
# plotando somente as outras linguagens
#sns.catplot(x='original_language', kind='count', data=nao_ingles)

sns.catplot(x='original_language', kind='count', data=nao_ingles, aspect=2, order=indice.index, palette='GnBu_d')
plt.show()