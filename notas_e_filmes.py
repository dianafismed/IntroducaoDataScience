import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

notas = pd.read_csv('./dados/ratings.csv')
notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']

filmes = pd.read_csv('./dados/movies.csv')
filmes.columns = ['filmeId', 'titulo', 'genero']

notas_filme1 = notas.query('filmeId==1')
notas_filme2 = notas.query('filmeId==2')
#print(len(notas_filme1),len(notas_filme2))

media_1 = notas_filme1.nota.mean()
media_2 = notas_filme2.nota.mean()
# print('Média filme 1 = %.2f' % media_1)
# print('Média filme 2 = %.2f' % media_2)
desvio_padrao_1 = notas_filme1.nota.std()
desvio_padrao_2 = notas_filme2.nota.std()

# sns.distplot(notas_filme1)
# sns.distplot(notas_filme2)
# sns.boxplot(data=notas_filme1)
# sns.boxplot(data=notas_filme2)
# sns.boxplot(x='filmeId', y='nota', data=notas.query('filmeId in [1,2,3]'))
sns.distplot(notas_filme1.nota)

# plt.hist(notas_filme1)
# plt.hist(notas_filme2)
# plt.boxplot([notas_filme1.nota, notas_filme2.nota])

plt.show()