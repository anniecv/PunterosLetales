def sumar_elementos(lista_numeros):
    return sum([x for x in lista_numeros])

print("Probando sumar_elementos...")

assert sumar_elementos([1, 2, 3, 4, 5]) == 15
assert sumar_elementos([10, -2, 5]) == 13
assert sumar_elementos([]) == 0
assert sumar_elementos([100]) == 100

print("Pruebas para sumar_elementos pasaron!")