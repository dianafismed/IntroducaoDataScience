import pandas as pd

import os
os.system('cls')

# Usando outra database
outro_filmes = pd.read_csv('./dados/tmdb_movies.csv', delimiter=',')
#print(outro_filmes.head())
print(outro_filmes.original_language.unique())
