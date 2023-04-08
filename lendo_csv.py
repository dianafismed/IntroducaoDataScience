import csv

arquivo = open('ratings.csv')
linhas = csv.reader(arquivo)

for i in linhas:
  print(i)

