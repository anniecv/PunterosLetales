def sumar_elementos(lista_numeros):
  acumulador_suma = 0
  for elemento_actual in lista_numeros:
      acumulador_suma += elemento_actual
  return acumulador_suma

print("Probando sumar_elementos...")
assert sumar_elementos([1, 2, 3, 4, 5]) == 15
assert sumar_elementos([10, -2, 5]) == 13
assert sumar_elementos([]) == 0
assert sumar_elementos([100]) == 100
print("¡Pruebas para sumar_elementos pasaron!")

print("\n--- Pruebas adicionales ---")
print(f"Suma de [1, 2, 3, 4, 5]: {sumar_elementos([1, 2, 3, 4, 5])}")
print(f"Suma de [10, -2, 5]: {sumar_elementos([10, -2, 5])}")
print(f"Suma de lista vacía []: {sumar_elementos([])}")
print(f"Suma de [100]: {sumar_elementos([100])}")
print(f"Suma de [-1, -2, -3]: {sumar_elementos([-1, -2, -3])}")
print(f"Suma de [0, 0, 0, 0]: {sumar_elementos([0, 0, 0, 0])}")
print("\nWeimar Valda - FIN DEL PROGRAMA SUMA DE ELEMENTOS")

def encontrar_mayor(lista_numeros):
  if not lista_numeros:
      return None
  mayor_temporal = lista_numeros[0]
  for elemento_actual in lista_numeros[1:]:
      if elemento_actual > mayor_temporal:
          mayor_temporal = elemento_actual
  return mayor_temporal

print("\nProbando encontrar_mayor...\n")
listas_de_prueba = [
  [1, 9, 2, 8, 3, 7],
  [-1, -9, -2, -8],
  [42, 42, 42],
  [],
  [5]
]

for lista in listas_de_prueba:
  resultado = encontrar_mayor(lista)
  print(f"Lista: {lista} -> Mayor encontrado: {resultado}")

assert encontrar_mayor([1, 9, 2, 8, 3, 7]) == 9
assert encontrar_mayor([-1, -9, -2, -8]) == -1
assert encontrar_mayor([42, 42, 42]) == 42
assert encontrar_mayor([]) == None
assert encontrar_mayor([5]) == 5
print("\n¡Pruebas para encontrar_mayor pasaron!")
print("\nWeimar Valda - FIN DEL PROGRAMA ENCUENTRA EL MAYOR ELEMENTO")

def contar_apariciones(lista, elemento_buscado):
  contador = 0
  for elemento in lista:
      if elemento == elemento_buscado:
          contador += 1
  return contador

print("\nProbando contar_apariciones...\n")
lista_ejemplo = [4, 2, 4, 3, 4, 5, 6, 2, 4, 7, 8, 4]
elementos_a_buscar = [4, 2, 9, 7]

for elemento in elementos_a_buscar:
  resultado = contar_apariciones(lista_ejemplo, elemento)
  print(f"Elemento '{elemento}' aparece {resultado} veces en la lista: {lista_ejemplo}")
print("\nWeimar Valda - FIN DEL PROGRAMA QUE CUENTA LAS VECES QUE APARECE UN ELEMENTO")

def invertir_lista(lista_original):
  lista_invertida = []
  for i in range(len(lista_original) - 1, -1, -1):
      lista_invertida.append(lista_original[i])
  return lista_invertida

print("\nProbando invertir_lista...\n")
lista_prueba = [1, 2, 3, 4, 5]
lista_resultante = invertir_lista(lista_prueba)
print(f"Lista original: {lista_prueba}")
print(f"Lista invertida: {lista_resultante}")

assert lista_resultante == [5, 4, 3, 2, 1]
assert lista_prueba == [1, 2, 3, 4, 5]
assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
assert invertir_lista([]) == []

print("¡Pruebas para invertir_lista pasaron!")
print("\nWeimar Valda - FIN DEL PROGRAMA QUE INVIERTE LOS ELEMENTOS DE UNA LISTA")
