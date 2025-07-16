comidas_favoritas = ['Pizza', 'Rabioles', 'Tacos']

def imprimir_lista(lista):
    print("\nLista de comidas favoritas:")
    for i, comida in enumerate(lista):
        print(f"{i + 1}. {comida}")
    print()

def modificar_lista(lista):
    imprimir_lista(lista)
    try:
        indice = int(input("¿Qué número de comida deseas modificar? (1, 2, 3...): ")) - 1
        if 0 <= indice < len(lista):
            nuevo_valor = input("¿Cuál es la nueva comida favorita?: ")
            lista[indice] = nuevo_valor
            print("Comida actualizada con éxito.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver lista de comidas favoritas")
        print("2. Modificar una comida")
        print("3. Salir")
        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            imprimir_lista(comidas_favoritas)
        elif opcion == '2':
            modificar_lista(comidas_favoritas)
        elif opcion == '3':
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
