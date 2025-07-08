numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

print(f"Tabla del {numero}")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
