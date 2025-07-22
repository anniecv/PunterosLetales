
def transponer_matriz(matriz):
  if not matriz or not matriz[0]:
    return []
  num_filas = len(matriz)
  num_columnas = len(matriz[0])
  matriz_transpuesta = []
  for j in range(num_columnas):
    nueva_fila=[]
    for i in range(num_filas):
      nueva_fila.append(matriz[i][j])
      matriz_transpuesta.append(nueva_fila)
    return matriz_transpuesta
  print(matriz_transpuesta)
#print("las pruebas pasaron")
#def test_transponer_matriz():
  m1=[[1,2,3],[4,5,6],]
  t1= transponer_matriz(m1)
  assert t1 == [[1,4],[2,5],[3,6]]
print("Prueba 1 pasada")
print("pruebas pasadas")

# Ejercicio 2: Verificar si una matriz es identidad
def es_identidad(matriz):
    # Requisito 1: Debe ser cuadrada
    num_filas = len(matriz)
    if num_filas == 0:
        return True  # Una matriz vacía es trivialmente identidad

    for i in range(num_filas):
        if len(matriz[i]) != num_filas:
            return False  # No es cuadrada

    # Requisito 2: Verificar la diagonal y los ceros
    for i in range(num_filas):
        for j in range(num_filas):
            if i == j:
                if matriz[i][j] != 1:
                    return False  # La diagonal no tiene 1
            else:
                if matriz[i][j] != 0:
                    return False  # Elemento fuera de la diagonal no es 0

    return True  # Cumple con todas las condiciones de identidad

# Pruebas
identidad = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
no_identidad = [[1, 0, 0], [0, 2, 0], [0, 0, 1]]
no_cuadrada = [[1, 0], [0, 1], [0, 0]]

assert es_identidad(identidad) == True
assert es_identidad(no_identidad) == False
assert es_identidad(no_cuadrada) == False

print("ejercicio 2: todas las pruebas pasaron")
print("¡Todas las pruebas pasaron correctamente!")


# Ejercicio 3: Verificar si una matriz es simétrica
def es_simetrica(matriz):
    # Requisito 1: Debe ser cuadrada
    num_filas = len(matriz)
    if num_filas == 0:
        return True  # Una matriz vacía es trivialmente simétrica

    for i in range(num_filas):
        if len(matriz[i]) != num_filas:
            return False  # No es cuadrada

    # Requisito 2: Comparar matriz[i][j] con matriz[j][i]
    for i in range(num_filas):
        for j in range(i + 1, num_filas):  # Solo verificar la parte superior
            if matriz[i][j] != matriz[j][i]:
                return False  # Con una diferencia basta

    return True  # Si todo coincide, es simétrica

# Pruebas
sim = [[1, 7, 3], [7, 4, -5], [3, -5, 6]]
no_sim = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
no_cuadrada = [[1, 2], [3, 4], [5, 6]]

assert es_simetrica(sim)
assert not es_simetrica(no_sim)
assert not es_simetrica(no_cuadrada)

print("ejercicio 3: todas las pruebas pasaron")
print("¡Pruebas para es_simetrica pasaron!")
print ("Fin del programa - Jim Requena")
