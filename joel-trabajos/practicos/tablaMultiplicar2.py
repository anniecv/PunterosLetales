def tabla_multiplicar(numero):
    """
    Devuelve una lista con la tabla de multiplicar del número dado del 1 al 10.
    """
    tabla = []
    for i in range(1, 11):
        resultado = numero * i
        tabla.append(resultado)
    return tabla

# ===== Pruebas unitarias =====
assert tabla_multiplicar(2) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], "Error en la tabla del 2"
assert tabla_multiplicar(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], "Error en la tabla del 5"
assert tabla_multiplicar(0) == [0] * 10, "Error en la tabla del 0"
assert tabla_multiplicar(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Error en la tabla del 1"
assert tabla_multiplicar(10) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], "Error en la tabla del 10"
assert tabla_multiplicar(-1) == [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], "Error en la tabla del -1"
assert tabla_multiplicar(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], "Error en la tabla del 3"

print("✅ Pruebas unitarias pasadas con éxito.")

# ===== Ejecución interactiva =====
num_tabla = int(input("Introduce el número de la tabla: "))
print(f"--- Tabla del {num_tabla} ---")
tabla = tabla_multiplicar(num_tabla)

for i, resultado in enumerate(tabla, start=1):
    print(f"{num_tabla} x {i} = {resultado}")

print("--- Fin del programa --- joel-trabajos ---")
