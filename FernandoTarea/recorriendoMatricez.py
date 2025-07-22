# Definimos la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Opción 1: Recorriendo con índices (acceso explícito a posición)
print("Recorrido con índices:")
for i in range(len(matriz)):  # Recorre las filas por índice
    for j in range(len(matriz[0])):  # Recorre las columnas por índice
        elemento = matriz[i][j]
        print(f"Elemento en ({i}, {j}) es {elemento}")

print("\nRecorrido por elementos (forma más 'Pythonica'):")
# Opción 2: Recorriendo directamente por filas y elementos
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea al final de cada fila
