# Definir una matriz de ejemplo (3x3)
matriz = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
    
# Recorrer cada fila y elemento (versión Pythonica)
for fila_actual in matriz:       # Bucle exterior toma cada lista-fila
    for elemento in fila_actual:  # Bucle interior toma cada elemento de esa fila
        print(elemento, end=" ")  # Imprime elementos en la misma línea separados por espacio
    print()                      # Salto de línea después de cada fila