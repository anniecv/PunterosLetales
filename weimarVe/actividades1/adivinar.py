import getpass

def verificar_adivinanza(numero_secreto, intento):
    """Devuelve una pista según la diferencia entre el intento y el número secreto."""
    if intento < numero_secreto:
        return "Demasiado bajo"
    elif intento > numero_secreto:
        return "Demasiado alto"
    else:
        return "Correcto"

assert verificar_adivinanza(7, 3) == "Demasiado bajo", "Error: se esperaba 'Demasiado bajo'"
assert verificar_adivinanza(7, 10) == "Demasiado alto", "Error: se esperaba 'Demasiado alto'"
assert verificar_adivinanza(7, 7) == "Correcto", "Error: se esperaba 'Correcto'"

print("Pruebas unitarias superadas correctamente.")

while True:
    try:
        
        entrada = getpass.getpass("Ingresa el número secreto (oculto, entre 0 y 99): ")
        numero_secreto = int(entrada)

        if numero_secreto > 99 or numero_secreto < 0:
            print("El número debe estar entre 0 y 99.")
            continue
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    print("Comienza el juego. Adivina el número secreto entre 0 y 99.")

    while True:
        try:
            intento = int(input("Tu intento: "))
            resultado = verificar_adivinanza(numero_secreto, intento)

            if resultado == "Correcto":
                print(f"¡Correcto! El número era {numero_secreto}.")
                break
            else:
                print(f"{resultado}. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    continuar = input("¿Deseas jugar otra ronda? (S/N): ").strip().lower()
    if continuar != 's':
        break

print("--- Fin del programa ---Weimar valda")
