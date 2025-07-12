lista_secreta = [7, 4, 36, 2, 5]

print("🎮 Bienvenido al juego de Ahorcado Lógico en Lista 🎮")
print("Debes adivinar la lista secreta de 5 números.")
print("No puedes verla directamente, pero puedes hacer preguntas en forma de código Python.")
print("En cada turno, puedes evaluar expresiones o intentar adivinar la lista completa.")
print("Escribe 'adivinar' para intentar adivinar la lista o 'salir' para terminar el juego.")
print("Ejemplo de instrucción: len(lista_secreta), lista_secreta[0], sum(lista_secreta[:3]), etc.\n")

while True:
    instruccion = input("Escribe tu instrucción en Python, 'adivinar' o 'salir': ").strip().lower()

    if instruccion == "salir":
        print("👋 Gracias por jugar. ¡Hasta la próxima!")
        print("La lista secreta era:", lista_secreta)
        break

    elif instruccion == "adivinar":
        intento = input("Ingresa tu intento de lista, separado por comas (o escribe 'salir' para terminar): ").strip()
        if intento.lower() == "salir":
            print("👋 Gracias por jugar. ¡Hasta la próxima!")
            break
        try:
            intento_lista = [int(x.strip()) for x in intento.split(",")]
            if intento_lista == lista_secreta:
                print("🎉 ¡Felicidades, has adivinado la lista secreta! 🎉")
                break
            else:
                print("❌ Lista incorrecta, sigue intentando.\n")
        except ValueError:
            print("⚠️ Entrada no válida. Asegúrate de usar solo números separados por comas.\n")

    else:
        try:
            # Evaluamos la instrucción en un entorno controlado
            resultado = eval(instruccion, {"__builtins__": {}}, {"lista_secreta": lista_secreta})
            print(f"✅ Resultado: {resultado}\n")
        except Exception as e:
            print(f"⚠️ Error en la instrucción: {e}\n")

  