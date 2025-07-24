
# Definimos la función que suma todos los elementos de una matriz
def sumar_total_matriz(matriz):
    """
    Esta función recibe una matriz (lista de listas)
    y retorna la suma total de todos sus elementos.
    Ejemplo:
    matriz = [[1, 2], [3, 4]]
    resultado = 10
    """
    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total

# Función para probar que sumar_total_matriz funciona correctamente
def probar_suma_total():
    print("Probando sumar_total_matriz...")

    # Caso 1: matriz normal
    m1 = [[1, 2, 3], [4, 5, 6]]
    assert sumar_total_matriz(m1) == 21  # 1+2+3+4+5+6 = 21

    # Caso 2: matriz con negativos y ceros
    m2 = [[-1, 0, 1], [10, -5, 5]]
    assert sumar_total_matriz(m2) == 10  # -1+0+1+10-5+5 = 10

    # Casos borde o límites
    assert sumar_total_matriz([[]]) == 0        # Matriz con una fila vacía
    assert sumar_total_matriz([]) == 0          # Matriz completamente vacía
    assert sumar_total_matriz([[42]]) == 42     # Matriz de un solo elemento

    print("¡Pruebas para sumar_total_matriz pasaron!")

# Llamamos a la función de pruebas
probar_suma_total()


#Ejercicio 2

# Definimos la función que suma los elementos por cada fila de la matriz
def sumar_por_filas(matriz):
    """
    Esta función recibe una matriz (lista de listas)
    y devuelve una lista con la suma de cada fila.
    Ejemplo:
    matriz = [[1, 2, 3], [4, 5, 6]]
    resultado = [6, 15]
    """
    resultado = []
    for fila in matriz:
        suma_fila = sum(fila)  # Suma todos los elementos de la fila
        resultado.append(suma_fila)
    return resultado

# Función de prueba para verificar que sumar_por_filas funciona correctamente
def probar_suma_por_filas():
    print("\nProbando sumar_por_filas...")

    # Caso 1: matriz con 3 filas y 3 columnas
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sumar_por_filas(m1) == [6, 15, 24]  # 1+2+3, 4+5+6, 7+8+9

    # Caso 2: matriz con pares repetidos
    m2 = [[10, 10], [20, 20], [30, 30]]
    assert sumar_por_filas(m2) == [20, 40, 60]

    # Caso borde: matriz vacía
    assert sumar_por_filas([]) == []  # No hay filas que sumar

    print("¡Pruebas para sumar_por_filas pasaron!")
    print("ejercicio 2: ¡Todo está correcto!")

# Llamamos a la función para ejecutar las pruebas
probar_suma_por_filas()


#EJERCICIO 3

# Definimos la función que suma los elementos de la diagonal principal de una matriz cuadrada
def sumar_diagonal_principal(matriz):
    """
    Esta función recibe una matriz cuadrada (misma cantidad de filas y columnas)
    y retorna la suma de los elementos en su diagonal principal.
    Ejemplo:
    matriz = [[1, 2],
              [3, 4]]
    diagonal principal: 1 y 4 → suma = 5
    """
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]  # Accede al elemento en la posición (i, i)
    return suma

# Función de prueba para verificar que sumar_diagonal_principal funciona correctamente
def probar_suma_diagonal_principal():
    print("\nProbando sumar_diagonal_principal...")

    # Caso 1: matriz 3x3 con números consecutivos
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sumar_diagonal_principal(m1) == 15  # 1 + 5 + 9

    # Caso 2: matriz 2x2 con ceros y valores definidos
    m2 = [[10, 0], [0, 20]]
    assert sumar_diagonal_principal(m2) == 30  # 10 + 20

    # Caso borde: matriz 1x1
    m3 = [[5]]
    assert sumar_diagonal_principal(m3) == 5  # Solo un elemento en la diagonal

    print("¡Pruebas para sumar_diagonal_principal pasaron!")
    print ("Fin del programa - Jim Requena")

# Llamamos a la función para ejecutar las pruebas
probar_suma_diagonal_principal()
