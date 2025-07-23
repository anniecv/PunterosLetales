# clase05_operaciones_listas.py

# Ejercicio 1: Sumar elementos de una lista
def sumar_elementos(lista_numeros):
    """
    Recibe una lista de números y retorna la suma total.
    """
    acumulador_suma = 0
    for elemento in lista_numeros:
        acumulador_suma += elemento
    return acumulador_suma


# Ejercicio 2: Encontrar el mayor elemento de una lista
def encontrar_mayor(lista_numeros):
    """
    Retorna el número más grande de la lista.
    Si la lista está vacía, retorna None.
    """
    if not lista_numeros:
        return None
    mayor = lista_numeros[0]
    for elemento in lista_numeros[1:]:
        if elemento > mayor:
            mayor = elemento
    return mayor


# Ejercicio 3: Contar cuántas veces aparece un elemento en una lista
def contar_apariciones(lista, elemento_buscado):
    """
    Cuenta las apariciones de elemento_buscado en lista.
    """
    contador = 0
    for elemento in lista:
        if elemento == elemento_buscado:
            contador += 1
    return contador


# Ejercicio 4: Invertir la posición de los elementos de una lista
def invertir_lista(lista_original):
    """
    Retorna una lista nueva con los elementos en orden inverso.
    No modifica lista_original.
    """
    lista_invertida = []
    for i in range(len(lista_original) - 1, -1, -1):
        lista_invertida.append(lista_original[i])
    return lista_invertida


# BLOQUE DE PRUEBAS
if __name__ == "__main__":
    # Pruebas para sumar_elementos
    print("Probando sumar_elementos...")
    assert sumar_elementos([1, 2, 3, 4, 5]) == 15
    assert sumar_elementos([10, -2, 5]) == 13
    assert sumar_elementos([]) == 0
    assert sumar_elementos([100]) == 100
    print("¡Pruebas para sumar_elementos pasaron! ✅\n")

    # Pruebas para encontrar_mayor
    print("Probando encontrar_mayor...")
    listas_de_prueba = [[1, 9, 2, 8, 3, 7], [-1, -9, -2, -8], [42, 42, 42], [], [5]]
    for lista in listas_de_prueba:
        resultado = encontrar_mayor(lista)
        print(f"Lista: {lista} -> Mayor encontrado: {resultado}")

    assert encontrar_mayor([1, 9, 2, 8, 3, 7]) == 9
    assert encontrar_mayor([-1, -9, -2, -8]) == -1
    assert encontrar_mayor([42, 42, 42]) == 42
    assert encontrar_mayor([]) is None
    assert encontrar_mayor([5]) == 5
    print("¡Pruebas para encontrar_mayor pasaron! ✅\n")

    # Pruebas para contar_apariciones
    print("Probando contar_apariciones...")
    lista_ejemplo = [4, 2, 4, 3, 4, 5, 6, 2, 4, 7, 8, 4]
    elementos_a_buscar = [4, 2, 9, 7]
    for elemento in elementos_a_buscar:
        resultado = contar_apariciones(lista_ejemplo, elemento)
        print(f"Elemento '{elemento}' aparece {resultado} veces en la lista: {lista_ejemplo}")
    print("FIN DEL PROGRAMA QUE CUENTA LAS VECES QUE APARECE UN ELEMENTO\n")

    # Pruebas para invertir_lista
    print("Probando invertir_lista...")
    lista_prueba = [1, 2, 3, 4, 5]
    lista_invertida = invertir_lista(lista_prueba)
    print(f"Lista original: {lista_prueba}")
    print(f"Lista invertida: {lista_invertida}")

    assert lista_invertida == [5, 4, 3, 2, 1]
    assert lista_prueba == [1, 2, 3, 4, 5]  # No se modificó la original
    assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
    assert invertir_lista([]) == []
    print("¡Pruebas para invertir_lista pasaron! ✅\n")