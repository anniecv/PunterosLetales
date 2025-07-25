def es_simetrica(matriz):
    num_filas = len(matriz)
    if num_filas == 0:
        return True
    for i in range(num_filas):
        if len(matriz[i]) != num_filas:
            return False
    for i in range(num_filas):
        for j in range(i + 1, num_filas):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

sim = [[1, 7, 3], [7, 4, -5], [3, -5, 6]]
no_sim = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
no_cuadrada = [[1, 2], [3, 4], [5, 6]]

assert es_simetrica(sim) == True
assert es_simetrica(no_sim) == False
assert es_simetrica(no_cuadrada) == False

print("Pruebas para es_simetrica pasaron")

def es_identidad(matriz):
    num_filas = len(matriz)
    if num_filas == 0:
        return True
    for i in range(num_filas):
        if len(matriz[i]) != num_filas:
            return False
    for i in range(num_filas):
        for j in range(num_filas):
            if i == j:
                if matriz[i][j] != 1:
                    return False
            else:
                if matriz[i][j] != 0:
                    return False
    return True

identidad = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
no_identidad = [[1, 0, 0], [0, 2, 0], [0, 0, 1]]
no_cuadrada = [[1, 0], [0, 1], [0, 0]]

assert es_identidad(identidad) == True
assert es_identidad(no_identidad) == False
assert es_identidad(no_cuadrada) == False

print("Pruebas para es_identidad pasaron")

def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    matriz_transpuesta = []
    for j in range(num_columnas):
        nueva_fila = []
        for i in range(num_filas):
            nueva_fila.append(matriz[i][j])
        matriz_transpuesta.append(nueva_fila)
    return matriz_transpuesta

m1 = [[1, 2, 3], [4, 5, 6]]
t1 = transponer_matriz(m1)
assert t1 == [[1, 4], [2, 5], [3, 6]]
print("Prueba 1 (2x3) pasada")
