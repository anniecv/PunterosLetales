import tkinter as tk
from tkinter import messagebox

# Tu código adaptado para la interfaz

FILAS = 5
COLUMNAS = 8

def crear_sala(filas, columnas):
    sala = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if 2 <= j <= 5:
                precio = 50
            else:
                precio = 30
            fila.append({"estado": "L", "precio": precio})
        sala.append(fila)
    return sala

class SalaGUI:
    def __init__(self, master):
        self.master = master
        self.sala = crear_sala(FILAS, COLUMNAS)
        self.master.title("Reserva de asientos - Cine")
        self.master.geometry("600x500")

        self.frame_sala = tk.Frame(master)
        self.frame_sala.pack(pady=10)

        self.labels_fila = []
        self.buttons = []  # para botones de asientos

        self.crear_tablero()

        self.frame_opciones = tk.Frame(master)
        self.frame_opciones.pack(pady=10)

        # Opciones individuales
        tk.Label(self.frame_opciones, text="Fila (0-index):").grid(row=0, column=0)
        self.entrada_fila = tk.Entry(self.frame_opciones, width=3)
        self.entrada_fila.grid(row=0, column=1)
        tk.Label(self.frame_opciones, text="Columna (0-index):").grid(row=0, column=2)
        self.entrada_columna = tk.Entry(self.frame_opciones, width=3)
        self.entrada_columna.grid(row=0, column=3)

        self.boton_ocupar = tk.Button(self.frame_opciones, text="Ocupar asiento individual", command=self.ocupar_individual)
        self.boton_ocupar.grid(row=0, column=4, padx=10)

        # Opciones para N asientos juntos
        tk.Label(self.frame_opciones, text="Asientos juntos:").grid(row=1, column=0)
        self.entrada_njuntos = tk.Entry(self.frame_opciones, width=5)
        self.entrada_njuntos.grid(row=1, column=1)
        self.boton_ocupar_juntos = tk.Button(self.frame_opciones, text="Buscar y reservar", command=self.ocupar_juntos)
        self.boton_ocupar_juntos.grid(row=1, column=4, padx=10)

        # Mostrar asientos libres
        self.label_libres = tk.Label(master, text=f"Asientos libres: {self.contar_asientos_libres()}")
        self.label_libres.pack(pady=10)

    def crear_tablero(self):
        # Limpia frame anterior si existiera
        for widget in self.frame_sala.winfo_children():
            widget.destroy()

        self.buttons = []
        for i in range(FILAS):
            fila_btns = []
            tk.Label(self.frame_sala, text=f"F{i}", width=3).grid(row=i+1, column=0)
            for j in range(COLUMNAS):
                color = self.get_color(self.sala[i][j]['estado'])
                texto = f"${self.sala[i][j]['precio']}"
                b = tk.Button(self.frame_sala, text=texto, bg=color, width=6, height=2,
                              command=lambda fila=i, col=j: self.toggle_asiento(fila, col))
                b.grid(row=i+1, column=j+1, padx=2, pady=2)
                fila_btns.append(b)
            self.buttons.append(fila_btns)

        # Encabezados de columnas
        for j in range(COLUMNAS):
            tk.Label(self.frame_sala, text=f"C{j}", width=6).grid(row=0, column=j+1)

    def get_color(self, estado):
        if estado == "L":
            return "green"
        elif estado == "O":
            return "red"
        else:
            return "grey"

    def toggle_asiento(self, fila, columna):
        asiento = self.sala[fila][columna]
        if asiento["estado"] == "L":
            result = messagebox.askyesno("Confirmar", f"¿Deseas reservar el asiento F{fila}C{columna} a Bs. {asiento['precio']}?")
            if result:
                asiento["estado"] = "O"
                self.actualizar_tablero()
        elif asiento["estado"] == "O":
            messagebox.showinfo("Info", "El asiento ya está ocupado.")

    def actualizar_tablero(self):
        for i in range(FILAS):
            for j in range(COLUMNAS):
                color = self.get_color(self.sala[i][j]['estado'])
                self.buttons[i][j].config(bg=color)
        self.label_libres.config(text=f"Asientos libres: {self.contar_asientos_libres()}")

    def ocupar_individual(self):
        try:
            fila = int(self.entrada_fila.get())
            columna = int(self.entrada_columna.get())
        except ValueError:
            messagebox.showerror("Error", "Fila y columna deben ser números enteros.")
            return

        if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
            if self.sala[fila][columna]["estado"] == "L":
                self.sala[fila][columna]["estado"] = "O"
                messagebox.showinfo("Éxito", f"Asiento F{fila}C{columna} reservado por Bs. {self.sala[fila][columna]['precio']}")
                self.actualizar_tablero()
            else:
                messagebox.showwarning("Advertencia", "Ese asiento ya está ocupado.")
        else:
            messagebox.showerror("Error", "Coordenadas fuera de rango.")

    def buscar_asientos_juntos(self, cantidad):
        for i, fila in enumerate(self.sala):
            consecutivos = 0
            inicio = 0
            for j, asiento in enumerate(fila):
                if asiento["estado"] == "L":
                    consecutivos += 1
                    if consecutivos == cantidad:
                        return i, j - cantidad + 1
                else:
                    consecutivos = 0
        return None, None

    def ocupar_juntos(self):
        try:
            n = int(self.entrada_njuntos.get())
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número entero.")
            return
        if n < 1 or n > COLUMNAS:
            messagebox.showerror("Error", f"Cantidad debe ser entre 1 y {COLUMNAS}.")
            return

        fila, inicio = self.buscar_asientos_juntos(n)
        if fila is not None:
            total = 0
            for j in range(inicio, inicio + n):
                self.sala[fila][j]["estado"] = "O"
                total += self.sala[fila][j]["precio"]
            messagebox.showinfo("Éxito", f"{n} asientos reservados en fila {fila}, columnas {inicio} a {inicio + n -1}\nTotal: Bs. {total}")
            self.actualizar_tablero()
        else:
            messagebox.showwarning("Sin asientos", "No hay suficientes asientos contiguos disponibles.")

    def contar_asientos_libres(self):
        return sum(asiento["estado"] == "L" for fila in self.sala for asiento in fila)

if __name__ == "__main__":
    root = tk.Tk()
    app = SalaGUI(root)
    root.mainloop()