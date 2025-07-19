  for fila in matriz:
      if fila != n:
          return False
  for i in range(n):
      for j in range(n):
          if matriz[i][j] != matriz[j][i]:
             return False
  return True

def es_matriz_simetrica(matriz):
  n = len(matriz)
