notas_parciales = []

cantidad = int(input("¿Cuántas notas querés ingresar? "))

for i in range(cantidad):
    nota = float(input(f"Ingresá la nota #{i + 1}: "))
    notas_parciales.append(nota)

print("\nNotas ingresadas:")
for i in range(len(notas_parciales)):
    print(f"Parcial {i + 1}: {notas_parciales[i]}")

print(f"\nCantidad total de notas: {len(notas_parciales)}")

promedio = sum(notas_parciales) / len(notas_parciales)
print(f"Promedio general: {promedio:.2f}")

nota_max = max(notas_parciales)
nota_min = min(notas_parciales)
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")

opcion = input("\n¿Querés modificar alguna nota? (s/n): ").lower()

if opcion == 's':
    indice_modificar = int(input("¿Qué número de parcial querés cambiar? (empezando desde 1): ")) - 1

    if 0 <= indice_modificar < len(notas_parciales):
        nueva_nota = float(input("Ingresá la nueva nota: "))
        notas_parciales[indice_modificar] = nueva_nota
        print("Nota actualizada con éxito.")
    else:
        print("Ese parcial no existe.")

print("\nNotas actualizadas:")
for i in range(len(notas_parciales)):
    print(f"Parcial {i + 1}: {notas_parciales[i]}")

