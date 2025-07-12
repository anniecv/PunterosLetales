import getpass
verificacion_de_Errores = ["len(lista_Secreta)", "lista_Secreta[2]", "lista_Secreta[0]> 10","adivinar", "me rindo"]
longitud_lista = int(input("Ingrese la longitud de la lista secreta (máximo 5): "))
if longitud_lista > 5:
    print("La longitud máxima de la lista es 5. Se ajustará a 5.")
    longitud_lista = 5

lista_Secreta = [0] * longitud_lista  # Inicializa una lista de la longitud especificada
for i in range(len(lista_Secreta)):
    lista_Secreta[i] = getpass.getpass(f"Ingrese el elemento {i+1} de la lista secreta (oculto): ")

print(" ¡bienvenido al juego del ahorcado logico con listas!")
print("debes descubrir que numeros hay en la lista secreta de 5 elementos")
print("pero no puedes verla directamemte. En cada turno puedes hacer una pregunta en forma de codigo Python")
print("ejemplo: len(lista_secreta), lista_secreta[2], lista_secreta[0]> 10")
print("cuando crees tener la lista completa, escribe 'adivinar' y luego tu adivinanza")

while True:
    instruccion = input(" escribe tu instruccion (o adivinar): ").strip().lower()
    if instruccion == "adivinar":
        intento = input(" escribe tu intrento de lista (separa por comas): ")
        try:
            intento_lista = [int(x.strip()) for x in intento.split(',')]
            if intento_lista == lista_Secreta:
                print("¡Felicidades! Has adivinado la lista secreta.")
                break
            else:
                print("Lo siento, tu adivinanza no es correcta.")
        except ValueError:
            print("Por favor, ingresa una lista de números válida separada por comas.")
    elif instruccion == "me rindo":
        print(f"La lista secreta era: {lista_Secreta}")
        print("--- Fin del programa --- Joel Trabajos ---")
        break
    elif instruccion != "len(lista_Secreta)" and instruccion not in verificacion_de_Errores:
        print("Instrucción no permitida. Intenta con otra.")
    else:
        try:
            resultado = eval(instruccion,{"lista_Secreta": lista_Secreta})
            print(f"Resultado de tu instrucción: {resultado}")
        except Exception as e:
            print(f"Error en tu instrucción: {e}")