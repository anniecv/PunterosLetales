# Lista vacía donde se guardarán las notas
notas_parciales = []

# Pedimos al usuario cuántas notas quiere ingresar
cantidad = int(input("¿Cuántas notas querés ingresar? "))

# Ingresamos cada nota con un bucle
for i in range(cantidad):
    nota = float(input(f"Ingresá la nota #{i + 1}: "))
    notas_parciales.append(nota)

# Mostramos todas las notas ingresadas
print("\nNotas ingresadas:")
for i in range(len(notas_parciales)):
    print(f"Parcial {i + 1}: {notas_parciales[i]}")

# Mostramos la cantidad total de notas
print(f"\nCantidad total de notas: {len(notas_parciales)}")

# Calculamos el promedio
promedio = sum(notas_parciales) / len(notas_parciales)
print(f"Promedio general: {promedio:.2f}")

# Buscamos la nota más alta y más baja
nota_max = max(notas_parciales)
nota_min = min(notas_parciales)
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")

# Opción para modificar una nota si fue recorrección, por ejemplo
opcion = input("\n¿Querés modificar alguna nota? (s/n): ").lower()

if opcion == 's':
    indice_modificar = int(input("¿Qué número de parcial querés cambiar? (empezando desde 1): ")) - 1

    # Verificamos que el índice esté dentro del rango válido
    if 0 <= indice_modificar < len(notas_parciales):
        nueva_nota = float(input("Ingresá la nueva nota: "))
        notas_parciales[indice_modificar] = nueva_nota
        print("Nota actualizada con éxito.")
    else:
        print("Ese parcial no existe.")

# Mostramos las notas finales
print("\nNotas actualizadas:")
for i in range(len(notas_parciales)):

