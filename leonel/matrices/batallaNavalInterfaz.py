import tkinter as tk
from tkinter import messagebox
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


class BatallaNavalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Batalla Naval")
        self.modo = None  # 1 = CPU, 2 = jugador vs jugador

        self.frame_menu = tk.Frame(master)
        self.frame_menu.pack(padx=10, pady=10)

        tk.Label(self.frame_menu, text="Selecciona modo:").pack()
        tk.Button(self.frame_menu, text="1. Jugar contra la CPU", command=self.comenzar_cpu).pack(fill='x', pady=5)
        tk.Button(self.frame_menu, text="2. Jugar contra otro jugador", command=self.comenzar_dos).pack(fill='x', pady=5)

        self.frame_juego = None

    def comenzar_cpu(self):
        self.modo = 1
        self.nombre_jugador = None
        self.nombre_cpu = "CPU"
        self.iniciar_juego()

    def comenzar_dos(self):
        self.modo = 2
        self.iniciar_pedir_nombres()

    def iniciar_pedir_nombres(self):
        self.frame_menu.pack_forget()

        self.frame_nombres = tk.Frame(self.master)
        self.frame_nombres.pack(padx=10, pady=10)

        tk.Label(self.frame_nombres, text="Nombre Jugador 1:").grid(row=0, column=0)
        self.entrada_nombre1 = tk.Entry(self.frame_nombres)
        self.entrada_nombre1.grid(row=0, column=1)

        tk.Label(self.frame_nombres, text="Nombre Jugador 2:").grid(row=1, column=0)
        self.entrada_nombre2 = tk.Entry(self.frame_nombres)
        self.entrada_nombre2.grid(row=1, column=1)

        tk.Button(self.frame_nombres, text="Comenzar", command=self.guardar_nombres).grid(row=2, column=0, columnspan=2, pady=5)

    def guardar_nombres(self):
        n1 = self.entrada_nombre1.get().strip()
        n2 = self.entrada_nombre2.get().strip()
        if not n1 or not n2:
            messagebox.showerror("Error", "Por favor, ingresa ambos nombres.")
            return
        self.nombre1 = n1
        self.nombre2 = n2
        self.frame_nombres.destroy()
        self.iniciar_juego()

    def iniciar_juego(self):
        if self.frame_menu:
            self.frame_menu.pack_forget()
        if hasattr(self, "frame_nombres"):
            self.frame_nombres.pack_forget()

        self.tablero_jugador = crear_tablero()
        self.tablero_cpu = crear_tablero()
        self.disparos_jugador = crear_tablero()
        self.disparos_cpu = crear_tablero()

        if self.modo == 2:
            self.tablero1 = crear_tablero()
            self.tablero2 = crear_tablero()
            self.disparos1 = crear_tablero()
            self.disparos2 = crear_tablero()

        colocar_barcos(self.tablero_jugador if self.modo == 1 else self.tablero1, BARCOS)
        colocar_barcos(self.tablero_cpu if self.modo == 1 else self.tablero2, BARCOS)

        self.turno = 1
        self.turno_actual = 1  # para modo 2

        self.frame_juego = tk.Frame(self.master)
        self.frame_juego.pack(padx=10, pady=10)

        self.label_turno = tk.Label(self.frame_juego, text=f"Turno {self.turno}")
        self.label_turno.pack()

        self.frame_tableros = tk.Frame(self.frame_juego)
        self.frame_tableros.pack(pady=10)

        self.crear_tablero_widgets()

        self.actualizar_tableros()

    def crear_tablero_widgets(self):
        # Tablero jugador o jugador1
        self.frame_tablero_jugador = tk.Frame(self.frame_tableros)
        self.frame_tablero_jugador.pack(side='left', padx=20)
        texto = "Tu tablero" if self.modo == 1 else f"Tablero {self.nombre1}"
        tk.Label(self.frame_tablero_jugador, text=texto).pack()
        self.botones_jugador = []
        for i in range(FILAS):
            fila_botones = []
            frame_fila = tk.Frame(self.frame_tablero_jugador)
            frame_fila.pack()
            for j in range(COLUMNAS):
                b = tk.Button(frame_fila, width=2, height=1, command=lambda f=i, c=j: self.jugador_dispara(f, c))
                b.grid(row=i, column=j, padx=2, pady=2)
                fila_botones.append(b)
            self.botones_jugador.append(fila_botones)

        # Tablero disparos jugador o jugador1
        self.frame_tablero_disp_jugador = tk.Frame(self.frame_tableros)
        self.frame_tablero_disp_jugador.pack(side='left', padx=20)
        texto_disp = "Tus disparos"
        tk.Label(self.frame_tablero_disp_jugador, text=texto_disp).pack()
        self.botones_disp_jugador = []
        for i in range(FILAS):
            fila_botones = []
            frame_fila = tk.Frame(self.frame_tablero_disp_jugador)
            frame_fila.pack()
            for j in range(COLUMNAS):
                l = tk.Label(frame_fila, width=2, height=1, relief='raised', bg='lightblue')
                l.grid(row=i, column=j, padx=2, pady=2)
                fila_botones.append(l)
            self.botones_disp_jugador.append(fila_botones)

        if self.modo == 2:
            # Tablero jugador 2
            self.frame_tablero_jugador2 = tk.Frame(self.frame_tableros)
            self.frame_tablero_jugador2.pack(side='left', padx=20)
            tk.Label(self.frame_tablero_jugador2, text=f"Tablero {self.nombre2}").pack()
            self.botones_jugador2 = []
            for i in range(FILAS):
                fila_botones = []
                frame_fila = tk.Frame(self.frame_tablero_jugador2)
                frame_fila.pack()
                for j in range(COLUMNAS):
                    b = tk.Button(frame_fila, width=2, height=1, command=lambda f=i, c=j: self.jugador2_dispara(f, c))
                    b.grid(row=i, column=j, padx=2, pady=2)
                    fila_botones.append(b)
                self.botones_jugador2.append(fila_botones)

            # Tablero disparos jugador2
            self.frame_tablero_disp_jugador2 = tk.Frame(self.frame_tableros)
            self.frame_tablero_disp_jugador2.pack(side='left', padx=20)
            tk.Label(self.frame_tablero_disp_jugador2, text="Tus disparos").pack()
            self.botones_disp_jugador2 = []
            for i in range(FILAS):
                fila_botones = []
                frame_fila = tk.Frame(self.frame_tablero_disp_jugador2)
                frame_fila.pack()
                for j in range(COLUMNAS):
                    l = tk.Label(frame_fila, width=2, height=1, relief='raised', bg='lightblue')
                    l.grid(row=i, column=j, padx=2, pady=2)
                    fila_botones.append(l)
                self.botones_disp_jugador2.append(fila_botones)

    def actualizar_tableros(self):
        # Actualizar tablero jugador (mostrar barcos y tocados)
        if self.modo == 1:
            tablero_real = self.tablero_jugador
            tablero_disp = self.disparos_jugador
        else:
            if self.turno_actual == 1:
                tablero_real = self.tablero1
                tablero_disp = self.disparos1
            else:
                tablero_real = self.tablero2
                tablero_disp = self.disparos2

        for i in range(FILAS):
            for j in range(COLUMNAS):
                estado = tablero_real[i][j]
                btn = self.botones_jugador[i][j]
                if estado == VACIO:
                    btn.config(text='0', bg='white')
                elif estado == BARCO:
                    btn.config(text='1', bg='lightgrey')
                elif estado == TOCADO:
                    btn.config(text='X', bg='red')
                elif estado == AGUA:
                    btn.config(text='*', bg='blue')

                # Mostrar disparos (labels)
                disp = tablero_disp[i][j]
                lb = self.botones_disp_jugador[i][j]
                if disp == VACIO or disp == BARCO:
                    lb.config(text='0', bg='lightblue')
                elif disp == TOCADO:
                    lb.config(text='X', bg='red')
                elif disp == AGUA:
                    lb.config(text='*', bg='blue')

        if self.modo == 2:
            # Tablero jugador2 (oculta barcos)
            tablero2_real = self.tablero2 if self.turno_actual == 1 else self.tablero1
            tablero2_disp = self.disparos2 if self.turno_actual == 1 else self.disparos1

            for i in range(FILAS):
                for j in range(COLUMNAS):
                    # Oculatar barcos con '0'
                    estado = (self.tablero2 if self.turno_actual == 1 else self.tablero1)[i][j]
                    btn2 = self.botones_jugador2[i][j]
                    if estado == VACIO:
                        btn2.config(text='0', bg='white')
                    elif estado == BARCO:
                        btn2.config(text='0', bg='lightgrey')
                    elif estado == TOCADO:
                        btn2.config(text='X', bg='red')
                    elif estado == AGUA:
                        btn2.config(text='*', bg='blue')

                    disp2 = (self.disparos2 if self.turno_actual == 1 else self.disparos1)[i][j]
                    lb2 = self.botones_disp_jugador2[i][j]
                    if disp2 == VACIO or disp2 == BARCO:
                        lb2.config(text='0', bg='lightblue')
                    elif disp2 == TOCADO:
                        lb2.config(text='X', bg='red')
                    elif disp2 == AGUA:
                        lb2.config(text='*', bg='blue')

    def jugador_dispara(self, fila, col):
        if self.modo == 1:
            if quedan_barcos(self.tablero_jugador) and quedan_barcos(self.tablero_cpu):
                coord = f"{chr(ord('A') + fila)}{col + 1}"
                if disparar(self.tablero_cpu, self.disparos_jugador, coord, self.nombre_jugador):
                    self.actualizar_tableros()
                    if not quedan_barcos(self.tablero_cpu):
                        messagebox.showinfo("Fin del juego", f"¡{self.nombre_jugador} gana!")
                        guardar_puntuacion(self.nombre_jugador)
                        self.master.destroy()
                        return
                    self.turno_cpu_juega()
        else:
            # modo 2, sólo jugador 1 puede disparar en su turno
            if self.turno_actual != 1:
                messagebox.showinfo("Turno", "No es tu turno.")
                return

            coord = f"{chr(ord('A') + fila)}{col + 1}"
            if disparar(self.tablero2, self.disparos1, coord, self.nombre1):
                self.actualizar_tableros()
                if not quedan_barcos(self.tablero2):
                    messagebox.showinfo("Fin del juego", f"¡{self.nombre1} gana!")
                    guardar_puntuacion(self.nombre1)
                    self.master.destroy()
                    return
                self.turno_actual = 2
                self.label_turno.config(text=f"Turno {self.turno} - {self.nombre2}")
                self.actualizar_tableros()

    def jugador2_dispara(self, fila, col):
        if self.modo != 2:
            return
        if self.turno_actual != 2:
            messagebox.showinfo("Turno", "No es tu turno.")
            return

        coord = f"{chr(ord('A') + fila)}{col + 1}"
        if disparar(self.tablero1, self.disparos2, coord, self.nombre2):
            self.actualizar_tableros()
            if not quedan_barcos(self.tablero1):
                messagebox.showinfo("Fin del juego", f"¡{self.nombre2} gana!")
                guardar_puntuacion(self.nombre2)
                self.master.destroy()
                return
            self.turno_actual = 1
            self.turno += 1
            self.label_turno.config(text=f"Turno {self.turno} - {self.nombre1}")
            self.actualizar_tableros()

    def turno_cpu_juega(self):
        self.master.after(1000, self._turno_cpu_jugar)

    def _turno_cpu_jugar(self):
        turno_cpu(self.tablero_jugador, self.disparos_cpu, self.nombre_cpu)
        self.actualizar_tableros()
        if not quedan_barcos(self.tablero_jugador):
            messagebox.showinfo("Fin del juego", f"¡La CPU gana!")
            guardar_puntuacion(self.nombre_cpu)
            self.master.destroy()
            return
        self.turno += 1
        self.label_turno.config(text=f"Turno {self.turno}")

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
        messagebox.showinfo("Error", "Coordenada inválida, intenta de nuevo.")
        return False  # disparo no válido

    fila, columna = indices

    if tablero_disparos[fila][columna] in (TOCADO, AGUA):
        messagebox.showinfo("Error", "Ya se disparó allí. Intenta otra coordenada.")
        return False

    if tablero_objetivo[fila][columna] == BARCO:
        tablero_objetivo[fila][columna] = TOCADO
        tablero_disparos[fila][columna] = TOCADO
        messagebox.showinfo("Tocado", f"{nombre} hizo ¡Tocado!")
    else:
        tablero_objetivo[fila][columna] = AGUA
        tablero_disparos[fila][columna] = AGUA
        messagebox.showinfo("Agua", f"{nombre} disparó al agua.")
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
            messagebox.showinfo("CPU", f"{nombre} dispara a {coord}")
            disparar(tablero_objetivo, tablero_disparos, coord, nombre)
            return
        intentos += 1
    messagebox.showinfo("CPU", f"{nombre} no encontró dónde disparar (tablero lleno).")

if __name__ == "__main__":
    root = tk.Tk()
    app = BatallaNavalGUI(root)
    root.mainloop()