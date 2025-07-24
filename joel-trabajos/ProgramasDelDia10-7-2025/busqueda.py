def busque_lineal(lista, clave):
    for i in range(len(lista)):
        if lista[i] == clave:
            return i
    return -1

mi_lista_desordenada = [10, 5, 42, 8, 17, 30, 25]
print("probando busqueda lineal...")

assert busque_lineal(mi_lista_desordenada, 42) == 2, "Error: 42 debería estar en la posición 2"
assert busque_lineal(mi_lista_desordenada, 100) == -1, "Error: 100 no debería estar en la lista"
assert busque_lineal(mi_lista_desordenada, 10) == 0, "Error: 10 debería estar en la posición 0"
assert busque_lineal(mi_lista_desordenada, 5) == 1, "Error: 5 debería estar en la posición 1"
print("Todas las pruebas pasaron correctamente.")

def busque_binaria(lista, clave):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if mi_lista_desordenada[medio] == clave:
            return medio
        elif mi_lista_desordenada[medio] < clave:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

assert busque_binaria(mi_lista_desordenada, 42) == 2, "Error: 42 debería estar en la posición 2"
assert busque_binaria(mi_lista_desordenada, 100) == -1, "Error: 100 no debería estar en la lista"
assert busque_binaria(mi_lista_desordenada, 10) == 0, "Error: 10 debería estar en la posición 0"
assert busque_binaria(mi_lista_desordenada, 5) == 1, "Error: 5 debería estar en la posición 1"
print("Todas las pruebas de búsqueda binaria pasaron correctamente.")