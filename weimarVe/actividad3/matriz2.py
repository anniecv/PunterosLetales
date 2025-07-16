# Definición de la matriz (del ejercicio anterior)
teclado = [[0, 2, 3],[4, 5, 6],[7, 8, 9]]

# Bucle anidado para imprimir la matriz como cuadrícula
for fila in teclado:         # Recorre cada fila de la matriz
    for elemento in fila:     # Recorre cada elemento de la fila actual
        print(elemento, end="\t")  # Imprime con tabulador (sin salto de línea)
    print()                  # Salto de línea después de cada fila