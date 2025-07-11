mis_notas = []

cantidad = int(input("¿Cuántas notas vas a ingresar (5 o 6)?: "))
for i in range(cantidad):
    nota = float(input(f"Ingresá la nota #{i + 1}: "))
    mis_notas.append(nota)

suma_total = 0

for nota in mis_notas:
    suma_total += nota
promedio = suma_total / len(mis_notas)
print(f"\nSuma total de notas: {suma_total}")
print(f"Promedio: {promedio:.2f}")

print(mis_notas[10])
