# Paso 1: Crear lista vacía
comidas_favoritas = []

# Pedir al usuario que ingrese 3 comidas favoritas
print("Ingresá tus 3 comidas bolivianas favoritas:")

for i in range(3):
    comida = input(f"Comida #{i + 1}: ")
    comidas_favoritas.append(comida)

# Paso 2: Imprimir la lista completa
print("\nLista completa de comidas favoritas:", comidas_favoritas)

# Paso 3: Imprimir la segunda comida favorita
print(f"Mi segunda comida favorita es: {comidas_favoritas[1]}")  # índice 1 para la segunda comida

# Paso 4: Permitir cambiar alguna comida por índice
indice_a_modificar = int(input("\n¿Querés cambiar alguna comida?:  "))

if 0 <= indice_a_modificar < len(comidas_favoritas):
    nueva_comida = input("Ingresá el nuevo nombre para esa comida: ")
    comidas_favoritas[indice_a_modificar] = nueva_comida
else:
    print("Índice inválido. No se cambio ninguna comida.")

# Paso 5: Imprimir la lista actualizada
print("\nLista actualizada de comidas favoritas:", comidas_favoritas)

# Paso 6: Imprimir la cantidad de elementos con len()
cantidad = len(comidas_favoritas)
print(f"Mi lista de comidas favoritas tiene {cantidad} elementos.")
