# Ejercicio 1

def sumar_total_matriz(matriz):
    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total

def probar_suma_total():
    print("Probando sumar_total_matriz...")

    m1 = [[1, 2, 3], [4, 5, 6]]
    assert sumar_total_matriz(m1) == 21

    m2 = [[-1, 0, 1], [10, -5, 5]]
    assert sumar_total_matriz(m2) == 10

    assert sumar_total_matriz([[]]) == 0
    assert sumar_total_matriz([]) == 0
    assert sumar_total_matriz([[42]]) == 42

    print("¡Pruebas para sumar_total_matriz pasaron!")

probar_suma_total()

# Ejercicio 2

def sumar_por_filas(matriz):
    resultado = []
    for fila in matriz:
        suma_fila = sum(fila)
        resultado.append(suma_fila)
    return resultado

def probar_suma_por_filas():
    print("\nProbando sumar_por_filas...")

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sumar_por_filas(m1) == [6, 15, 24]

    m2 = [[10, 10], [20, 20], [30, 30]]
    assert sumar_por_filas(m2) == [20, 40, 60]

    assert sumar_por_filas([]) == []

    print("¡Pruebas para sumar_por_filas pasaron!")
    print("ejercicio 2: ¡Todo está correcto!")

probar_suma_por_filas()

# Ejercicio 3

def sumar_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

def probar_suma_diagonal_principal():
    print("\nProbando sumar_diagonal_principal...")

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sumar_diagonal_principal(m1) == 15

    m2 = [[10, 0], [0, 20]]
    assert sumar_diagonal_principal(m2) == 30

    m3 = [[5]]
    assert sumar_diagonal_principal(m3) == 5

    print("¡Pruebas para sumar_diagonal_principal pasaron!")
    print("Fin del programa - Weimar Valda")

probar_suma_diagonal_principal()
