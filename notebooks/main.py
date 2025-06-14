import pandas as pd

# Lendo o arquivo
df = pd.read_csv("data/Sample-Superstore.csv", encoding='latin1')

# Mostrando as primeiras linhas
print("Primeiras linhas do DataFrame:")
print(df.head())

# Informações iniciais
print("\nInformações do DataFrame:")
print(df.info())

# Verificando valores ausentes
print("\nValores ausentes por coluna:")
print(df.isnull().sum())