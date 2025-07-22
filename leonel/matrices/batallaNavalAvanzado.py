import random

FILAS = 4
COLUMNAS = 2
BARCOS = 3

VACIO = 0
BARCO = 1
TOCADO = 2
AGUA = 3

def crear_tablero():
    return [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]

def mostrar_tablero(tablero, ocultar_barcos=False):
    print("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for fila_idx, fila in enumerate(tablero):
        letra = chr(ord('A') + fila_idx)
        fila_mostrar = []
        for celda in fila:
            if celda == VACIO:
                fila_mostrar.append("0")
            elif celda == BARCO:
                fila_mostrar.append("0" if ocultar_barcos else "1")
            elif celda == TOCADO:
                fila_mostrar.append("X")
            elif celda == AGUA:
                fila_mostrar.append("*")
        print(letra + " " + " ".join(fila_mostrar))

def coord_a_indices(coord):
    if len(coord) < 2:
        return None
    fila = ord(coord[0].upper()) - ord('A')
    try:
        columna = int(coord[1:]) - 1
    except ValueError:
        return None
    if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
        return fila, columna
    return None

def colocar_barcos(tablero, cantidad):
    colocados = 0
    while colocados < cantidad:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == VACIO:
            tablero[fila][columna] = BARCO
            colocados += 1

def disparar(tablero_objetivo, tablero_disparos, coord, nombre):
    indices = coord_a_indices(coord)
    if indices is None:
        print("Coordenada inválida. Intenta de nuevo.")
        return False  # disparo no válido

    fila, columna = indices

    if tablero_disparos[fila][columna] in (TOCADO, AGUA):
        print("Ya se disparó allí. Intenta otra coordenada.")
        return False

    if tablero_objetivo[fila][columna] == BARCO:
        tablero_objetivo[fila][columna] = TOCADO
        tablero_disparos[fila][columna] = TOCADO
        print(f"{nombre} hizo ¡Tocado!")
    else:
        tablero_objetivo[fila][columna] = AGUA  # Opcional, para marcar tablero real
        tablero_disparos[fila][columna] = AGUA
        print(f"{nombre} disparó al agua.")
    return True

def quedan_barcos(tablero):
    return any(BARCO in fila for fila in tablero)

def guardar_puntuacion(nombre):
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre} ganó la partida.\n")

def turno_cpu(tablero_objetivo, tablero_disparos, nombre):
    intentos = 0
    max_intentos = FILAS * COLUMNAS * 2  # para evitar loop infinito
    while intentos < max_intentos:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero_disparos[fila][columna] not in (TOCADO, AGUA):
            coord = f"{chr(ord('A') + fila)}{columna + 1}"
            print(f"{nombre} dispara a {coord}")
            disparar(tablero_objetivo, tablero_disparos, coord, nombre)
            return
        intentos += 1
    print(f"{nombre} no encontró dónde disparar (tablero lleno).")

def juego():
    print("=== Batalla Naval ===")
    print("1. Jugar contra la CPU")
    print("2. Jugar contra otro jugador")
    modo = input("Selecciona modo (1 o 2): ")

    if modo == "1":
        nombre_jugador = input("Tu nombre: ")
        nombre_cpu = "CPU"

        tablero_jugador = crear_tablero()
        tablero_cpu = crear_tablero()
        disparos_jugador = crear_tablero()
        disparos_cpu = crear_tablero()

        colocar_barcos(tablero_jugador, BARCOS)
        colocar_barcos(tablero_cpu, BARCOS)

        turno = 1
        while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_cpu):
            print(f"\n--- Turno {turno} ---")

            print("\nTu tablero:")
            mostrar_tablero(tablero_jugador)
            print("\nTus disparos:")
            mostrar_tablero(disparos_jugador, ocultar_barcos=True)

            while True:
                coord = input("Dispara (ej. A1): ")
                if disparar(tablero_cpu, disparos_jugador, coord, nombre_jugador):
                    break

            if not quedan_barcos(tablero_cpu):
                break

            turno_cpu(tablero_jugador, disparos_cpu, nombre_cpu)
            if not quedan_barcos(tablero_jugador):
                break

            turno += 1

        if quedan_barcos(tablero_jugador):
            print(f"¡{nombre_jugador} gana!")
            guardar_puntuacion(nombre_jugador)
        else:
            print("¡La CPU gana!")

    elif modo == "2":
        nombre1 = input("Nombre del Jugador 1: ")
        nombre2 = input("Nombre del Jugador 2: ")

        tablero1 = crear_tablero()
        tablero2 = crear_tablero()
        disparos1 = crear_tablero()
        disparos2 = crear_tablero()

        colocar_barcos(tablero1, BARCOS)
        colocar_barcos(tablero2, BARCOS)

        turno = 1
        while quedan_barcos(tablero1) and quedan_barcos(tablero2):
            print(f"\n--- Turno {turno} ---")

            print(f"\n{nombre1}, este es tu tablero:")
            mostrar_tablero(tablero1)
            print("\nTus disparos:")
            mostrar_tablero(disparos1, ocultar_barcos=True)
            while True:
                coord = input(f"{nombre1}, dispara (ej. A1): ")
                if disparar(tablero2, disparos1, coord, nombre1):
                    break

            if not quedan_barcos(tablero2):
                break

            print(f"\n{nombre2}, este es tu tablero:")
            mostrar_tablero(tablero2)
            print("\nTus disparos:")
            mostrar_tablero(disparos2, ocultar_barcos=True)
            while True:
                coord = input(f"{nombre2}, dispara (ej. A1): ")
                if disparar(tablero1, disparos2, coord, nombre2):
                    break

            turno += 1

        if quedan_barcos(tablero2):
            print(f"¡{nombre1} gana!")
            guardar_puntuacion(nombre1)
        else:
            print(f"¡{nombre2} gana!")
            guardar_puntuacion(nombre2)
    else:
        print("Opción inválida. Reinicia el programa.")

if __name__ == "__main__":
    juego()