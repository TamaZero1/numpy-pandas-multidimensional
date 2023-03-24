import pandas as pd

# Crear una serie simple
s = pd.Series([1, 2, 3, 4, 5])
print("Serie simple:\n", s)

# Crear una serie con índices personalizados
s_index = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("Serie con índices personalizados:\n", s_index)
