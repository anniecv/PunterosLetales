# Ejercicio 2: Inventario

# 1. Crear una lista vacía llamada inventario
inventario = []

# 2. Crear 3 productos (diccionarios distintos)
producto1 = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor": "El Ceibo Ltda."
}

producto2 = {
    "codigo": "P002",
    "nombre": "Café de los Yungas",
    "precio_unitario": 35.50,
    "stock": 100,
    "proveedor": "Yungas Coffee"
}

producto3 = {
    "codigo": "P003",
    "nombre": "Quinua Real en Grano",
    "precio_unitario": 28.75,
    "stock": 80,
    "proveedor": "Quinua Bolivia S.A."
}

# 3. Agregarlos a la lista inventario
inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)

# 4. Imprimir cantidad de productos
print(f"\nCantidad de productos en inventario: {len(inventario)}")

# 5. Recorrer la lista e imprimir resumen
print("\n--- Inventario Actual ---")
for producto in inventario:
    print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")
