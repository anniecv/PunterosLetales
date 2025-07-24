matriz = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
 # Opción 1: Recorriendo con índices
num_filas = len(matriz)
num_columnas = len(matriz[0])
for i in range(num_filas):      # Bucle exterior para índices de fila (0, 1, 2)
    for j in range(num_columnas): # Bucle interior para índices de columna (0, 1, 2)
        elemento = matriz[i][j]
        print(f"Elemento en ({i},{j}) es {elemento}")
 # Opción 2: Recorriendo por elemento (más "Pythonico")
for fila_actual in matriz:      # Bucle exterior toma cada lista-fila
    for elemento in fila_actual:  # Bucle interior toma cada elemento de esa fila
            print(elemento, end=" ") # "end=' '" para imprimir en la misma línea
    print()

matriz = [ [col + fila * 5+ 1 for col in range(5)] for fila in range(5) ]
for fila in matriz:
     print("".join(str(x) for x in fila))  # Imprime cada fila como una cadena separada por espacios

