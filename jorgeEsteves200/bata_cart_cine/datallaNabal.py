import random

def crear_tablero(tamaño):
    return [["~"] * tamaño for _ in range(tamaño)]

def imprimir_tablero(tablero, mostrar_barcos=False):
    print("  " + " ".join(str(i) for i in range(len(tablero))))
    for i, fila in enumerate(tablero):
        visible = [
            celda if celda != "B" or mostrar_barcos else "~"
            for celda in fila
        ]
        print(f"{i} " + " ".join(visible))

def colocar_barcos(tablero, longitudes):
    tamaño = len(tablero)
    for largo in longitudes:
        colocado = False
        while not colocado:
            orientacion = random.choice(['H', 'V'])
            if orientacion == 'H':
                fila = random.randint(0, tamaño - 1)
                col = random.randint(0, tamaño - largo)
                if all(tablero[fila][col + i] == "~" for i in range(largo)):
                    for i in range(largo):
                        tablero[fila][col + i] = "B"
                    colocado = True
            else:
                fila = random.randint(0, tamaño - largo)
                col = random.randint(0, tamaño - 1)
                if all(tablero[fila + i][col] == "~" for i in range(largo)):
                    for i in range(largo):
                        tablero[fila + i][col] = "B"
                    colocado = True

def turno_jugador(tablero, oculto, nombre):
    print(f"\nTurno de {nombre}")
    while True:
        try:
            x = int(input("Fila: "))
            y = int(input("Columna: "))
            if oculto[x][y] in ["X", "O"]:
                print("Ya intentaste esa posición.")
                continue
            if oculto[x][y] == "B":
                print("¡Tocado!")
                oculto[x][y] = "X"
                tablero[x][y] = "X"
                return True
            else:
                print("Agua.")
                oculto[x][y] = "O"
                tablero[x][y] = "O"
                return False
        except (IndexError, ValueError):
            print("Coordenadas inválidas. Intenta de nuevo.")

def quedan_barcos(tablero):
    return any("B" in fila for fila in tablero)

def juego_dos_jugadores():
    tamaño = 6
    longitudes_barcos = [3, 2, 2]

    tableros = [crear_tablero(tamaño), crear_tablero(tamaño)]
    ocultos = [crear_tablero(tamaño), crear_tablero(tamaño)]
    nombres = [input("Nombre del Jugador 1: "), input("Nombre del Jugador 2: ")]

    print("\nColocando barcos para ambos jugadores...\n")
    for i in range(2):
        colocar_barcos(tableros[i], longitudes_barcos)

    turno = 0
    while True:
        enemigo = 1 - turno
        imprimir_tablero(ocultos[enemigo])
        tocado = turno_jugador(ocultos[enemigo], tableros[enemigo], nombres[turno])
        if not quedan_barcos(tableros[enemigo]):
            print(f"\n¡{nombres[turno]} ha ganado! Todos los barcos enemigos fueron hundidos.")
            print("Tablero final del oponente:")
            imprimir_tablero(tableros[enemigo], mostrar_barcos=True)
            break
        if not tocado:
            turno = enemigo

# Menú principal
try:
    menu = int(input("Seleccione una opción:\n1. Desea jugar\n2. Desea salir\nOpción: "))

    if menu == 1:
        opcion_jugar = int(input("¿Qué jugador desea ser? (1 o 2): "))

        if opcion_jugar == 1:
            print("Bienvenido Jugador 1")
            print("Tienes cartucho: 10 disparos")
            print("Tienes barcos: 4 barcos")
            juego_dos_jugadores()

        elif opcion_jugar == 2:
            print("Bienvenido Jugador 2")
            print("Tienes cartucho: 10 disparos")
            print("Tienes barcos: 4 barcos")
            juego_dos_jugadores()

        else:
            print("Opción de jugador no válida.")

    elif menu == 2:
        print("Hasta luego.")

    else:
        print("Opción de menú no válida.")

except ValueError:
    print("Entrada no válida. Por favor, ingrese un número.")