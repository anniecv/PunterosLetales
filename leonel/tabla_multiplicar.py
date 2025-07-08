num_tabla = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {num_tabla}")

for i in range(1, 11):
    resultado = num_tabla * i
    print(f"{num_tabla} x {i} = {resultado}")