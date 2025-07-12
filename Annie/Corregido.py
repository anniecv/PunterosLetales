def ingresar_lista_secreta():
    print("👨‍🏫 Ingreso de la lista secreta (NO visible para los estudiantes)")
    while True:
        try:
            cantidad = int(input("¿Cuántos elementos tendrá la lista secreta?: "))
            if cantidad < 1:
                print("⚠️ Debes ingresar al menos un elemento.")
            else:
                break
        except ValueError:
            print("⚠️ Ingresa un número válido.")

    while True:
        entrada = input(f"👉 Ingresa exactamente {cantidad} números separados por coma: ")
        try:
            lista = [int(x.strip()) for x in entrada.split(",") if x.strip() != ""]
            if len(lista) != cantidad:
                print(f"⚠️ Debes ingresar exactamente {cantidad} elementos. Ingresaste {len(lista)}.")
            else:
                break
        except ValueError:
            print("⚠️ Asegúrate de ingresar solo números separados por comas.")
    
    print(f"\n✅ Lista secreta de {cantidad} elementos cargada correctamente.\n")
    return lista

def mostrar_instrucciones(lista_secreta):
    print("🕵️‍♀️ ¡Bienvenidos al juego del Ahorcado Lógico con Listas!")
    print(f"La lista secreta tiene {len(lista_secreta)} elementos.")
    print("En cada turno puedes hacer una 'pregunta' en forma de código Python.")
    print("Ejemplos: len(lista_secreta), lista_secreta[2], lista_secreta[0] > 10")
    print("Cuando creas tener la lista completa, escribe: adivinar")
    print("--------------------------------------------------------------")

def jugar(lista_secreta):
    while True:
        instruccion = input(">>> Escribe tu instrucción (o 'adivinar'): ").strip()

        if instruccion.lower() == "adivinar":
            intento = input("🧠 Escribe tu intento de lista (separa por comas): ")
            numeros_crudos = [x.strip() for x in intento.split(",") if x.strip() != ""]
            try:
                intento_lista = [int(x) for x in numeros_crudos]
            except ValueError:
                print("⚠️ Error: asegúrate de escribir solo números válidos separados por comas.")
                continue

            if len(intento_lista) != len(lista_secreta):
                print(f"⚠️ Debes ingresar exactamente {len(lista_secreta)} números. Ingresaste {len(intento_lista)}.")
                continue

            if intento_lista == lista_secreta:
                print("🎉 ¡Correcto! Has descubierto la lista secreta.")
                break
            else:
                print("❌ Esa no es la lista correcta. Aquí tienes una pista:")
                aciertos = 0
                for i in range(len(lista_secreta)):
                    if intento_lista[i] == lista_secreta[i]:
                        print(f"✅ Posición {i}: correcto ({intento_lista[i]})")
                        aciertos += 1
                    else:
                        print(f"❌ Posición {i}: incorrecto (tuviste {intento_lista[i]})")
                print(f"🔎 Aciertos totales: {aciertos} de {len(lista_secreta)}")
        else:
            if not instruccion.strip():
                print("⚠️ No escribiste ninguna instrucción.")
                continue

            # Detecta si parece un intento de lista sin 'adivinar'
            if all(char.isdigit() or char.isspace() or char == ',' for char in instruccion):
                print("⚠️ Parece que intentaste escribir una lista. Usa 'adivinar' para hacer un intento.")
                continue

            try:
                resultado = eval(instruccion, {"lista_secreta": lista_secreta})
                print("Resultado:", resultado)
            except Exception as e:
                print("⚠️ Error en tu instrucción:", e)

def juego_completo():
    while True:
        lista_secreta = ingresar_lista_secreta()
        mostrar_instrucciones(lista_secreta)
        jugar(lista_secreta)

        jugar_otra_vez = input("🔁 ¿Quieres jugar otra vez con una nueva lista secreta? (s/n): ").strip().lower()
        if jugar_otra_vez != 's':
            print("👋 ¡Gracias por jugar! Hasta la próxima.")
            break

# ===================== INICIO DEL JUEGO ========================
juego_completo()
