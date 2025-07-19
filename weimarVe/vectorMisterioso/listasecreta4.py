import getpass

print("Ingreso de la lista secreta (NO visible para los estudiantes)")

while True:
    try:
        try:
            entrada_oculta = getpass.getpass("Ingrese los números secretos separados por comas (oculto): ")
        except Exception:
            print("Entrada oculta no compatible en este entorno. Usando entrada visible.")
            entrada_oculta = input("Ingrese los números secretos separados por comas (visible): ")

        lista_secreta = [int(x.strip()) for x in entrada_oculta.split(",") if x.strip() != '']

        if not lista_secreta:
            print("La lista no puede estar vacía.")
        else:
            break
    except ValueError:
        print("Error: asegúrate de ingresar solo números enteros separados por comas.")

print(f"\nLista secreta de {len(lista_secreta)} elementos cargada correctamente.\n")

print("¡Bienvenidos al juego del Ahorcado Lógico con Listas!")
print(f"La lista secreta tiene {len(lista_secreta)} elementos.")
print("En cada turno puedes hacer una 'pregunta' en forma de código Python.")
print("Ejemplos: len(lista_secreta), lista_secreta[2], lista_secreta[0] > 10")
print("Cuando creas tener la lista completa, escribe: adivinar")
print("Si te rindes, puedes escribir: lo siento")
print("--------------------------------------------------------------")

while True:
    instruccion = input(">>> Escribe tu instrucción (o 'adivinar' / 'lo siento'): ").strip().lower()

    if instruccion == "adivinar":
        intento = input("Escribe tu intento de lista (separa por comas): ")
        try:
            intento_lista = [int(x.strip()) for x in intento.split(",")]

            if intento_lista == lista_secreta:
                print("¡Correcto! Has descubierto la lista secreta.")
                break
            else:
                print("Esa no es la lista correcta.")
                aciertos = 0
                for i in range(len(lista_secreta)):
                    if i < len(intento_lista):
                        if intento_lista[i] == lista_secreta[i]:
                            print(f"Posición {i}: correcto ({intento_lista[i]})")
                            aciertos += 1
                        else:
                            print(f"Posición {i}: incorrecto (tuviste {intento_lista[i]}, se esperaba otro número)")
                    else:
                        print(f"Faltó ingresar un número en la posición {i}")
                print(f"Aciertos totales: {aciertos} de {len(lista_secreta)}")
        except ValueError:
            print("Error: asegúrate de ingresar solo números separados por comas.")

    elif instruccion == "lo siento":
        print("Gracias por jugar. Aquí estaba la lista secreta:")
        print("Lista secreta:", lista_secreta)
        break

    else:
        try:
            resultado = eval(instruccion, {"lista_secreta": lista_secreta})
            print("Resultado:", resultado)
        except Exception as e:
            print("Error en tu instrucción:", e)