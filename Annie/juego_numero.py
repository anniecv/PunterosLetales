# ===== Juego interactivo con múltiples rondas =====
while True:
    try:
        try:
            import getpass
            entrada = getpass.getpass("🔐 Ingresa el número secreto (oculto, máx 99): ")
        except Exception:
            print("⚠️ El entorno no soporta entrada oculta. Se usará entrada visible.")
            entrada = input("Ingresa el número secreto (visible, máx 99): ")

        numero_secreto = int(entrada)

        if numero_secreto > 99 or numero_secreto < 0:
            print("⚠️ El número debe estar entre 0 y 99.")
            continue
    except ValueError:
        print("⚠️ Ingresa un número válido.")
        continue

    print("🎯 ¡Adivina el número secreto entre 0 y 99!")

    while True:
        try:
            intento = int(input("Tu intento: "))
            resultado = verificar_adivinanza(numero_secreto, intento)

            if resultado == "Correcto":
                print(f"🎉 ¡Correcto! El número era {numero_secreto}.")
                break
            else:
                print(f"❌ {resultado}. Intenta de nuevo.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")

    continuar = input("¿Deseas jugar otra ronda? (Y/N): ").strip().lower()
    if continuar != 'y':
        break

print("--- Fin del programa --- ")
