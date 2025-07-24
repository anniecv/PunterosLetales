def es_matriz_simetrica(matriz):
    n = len(matriz)
    #verificar si es cuadrada
    if any(len(fila) != n for fila in matriz):
        return False  # No es cuadrada
    #verificar simetria usando comprension de listas
    return all(matriz[i][j] == matriz[j][i] for i in range(n) for j in range(i,n))