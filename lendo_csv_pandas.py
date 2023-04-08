import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

notas = pd.read_csv('./dados/ratings.csv')   # é um panda dataframe
#print(notas)
#print(notas.head())  # mostra os 5 primeiros registros
#print(notas.shape)   # mostra a qtde linhas, qtde colunas (formato)

notas.columns=('usuarioId', 'filmeId', 'nota', 'momento')   # muda o nome das colunas
#print(notas) # devolve uma serie
#print(notas['nota'])  
#print(notas['nota'].unique())
#print(notas['nota'].value_counts())   # mostra as notas e a qtde de cada nota e já ordena do mais frequente para o menos
#print(notas['nota'].mean())   # média das notas
#print(notas.nota)

#print(notas.nota.describe())

# mostra um histograma
# notas.nota.plot(kind='hist')
# plt.show()

# outro tipo de gráfico
sns.boxplot(notas.nota)
plt.show()