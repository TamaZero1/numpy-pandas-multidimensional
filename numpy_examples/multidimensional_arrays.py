import numpy as np

# Crear un arreglo bidimensional
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Arreglo bidimensional:\n", arr_2d)

# Acceder a elementos
print("Elemento en la posición (0, 1):", arr_2d[0, 1])

# Rebanar arreglos
print("Primeras dos filas y todas las columnas:\n", arr_2d[:2, :])