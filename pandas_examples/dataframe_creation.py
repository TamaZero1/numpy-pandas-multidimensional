import pandas as pd

# Crear un DataFrame simple a partir de un diccionario
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)
print("DataFrame simple:\n", df)

# Seleccionar una columna
print("Columna A:\n", df['A'])

# Seleccionar varias columnas
print("Columnas A y B:\n", df[['A', 'B']])

# Seleccionar filas por índice
print("Fila 0:\n", df.loc[0])

# Seleccionar filas por condición
print("Filas con valores en columna A mayores a 1:\n", df[df['A'] > 1])