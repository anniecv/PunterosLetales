def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    mitad_izquierda = lista[:medio]
    mitad_derecha = lista[medio:]

    izquierda_ordenada = merge_sort(mitad_izquierda)
    derecha_ordenada = merge_sort(mitad_derecha)

    print(f"Mezclaría {izquierda_ordenada} y {derecha_ordenada}")
    return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

lista_prueba = [8, 3, 5, 1]
print("Lista original:", lista_prueba)
resultado = merge_sort(lista_prueba)
print("Lista ordenada:", resultado)

assert merge_sort([]) == []
assert merge_sort([1]) == [1]
assert merge_sort([5, 2]) == [2, 5]
assert merge_sort([3, 1, 2]) == [1, 2, 3]
assert merge_sort([10, 5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8, 10]
assert merge_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert merge_sort([4, 2, 2, 4, 1]) == [1, 2, 2, 4, 4]
assert merge_sort([100, -50, 0, 50, -100]) == [-100, -50, 0, 50, 100]
assert merge_sort([2.5, 1.2, 3.8]) == [1.2, 2.5, 3.8]

print("¡Todas las pruebas con assert pasaron correctamente!")
print("Weimar Valda - FIN DEL PROGRAMA")