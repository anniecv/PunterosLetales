def invertir_lista(lista_original):
  # Paso 1: Crear una nueva lista vacía
  lista_invertida = []

  # Paso 2: Recorrer la lista original desde el final hacia el inicio
  for i in range(len(lista_original) - 1, -1, -1):
      # Paso 3: Añadir el elemento actual a la lista_invertida
      lista_invertida.append(lista_original[i])

  # Paso 5: Retornar la lista invertida
  return lista_invertida

# Ejemplo de uso
mi_lista = [10, 20, 30, 40, 50]
resultado = invertir_lista(mi_lista)
print("Lista original:", mi_lista)
print("Lista invertida:", resultado)

print("\nProbando invertir_lista...")
lista_prueba = [1, 2, 3, 4, 5]
lista_resultante = invertir_lista(lista_prueba)
assert lista_resultante == [5, 4, 3, 2, 1]
assert lista_prueba == [1, 2, 3, 4, 5] # ¡Verifica que la original no cambió!
assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
assert invertir_lista([]) == []
print("¡Pruebas para invertir_lista pasaron! ")
