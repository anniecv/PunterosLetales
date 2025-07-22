# Ejercicio 3: Operaciones CRUD en inventario

def buscar_producto(inventario, codigo):
    for producto in inventario:
        if producto["codigo"] == codigo:
            return producto
    return None

def actualizar_stock(inventario, codigo, nueva_cantidad):
    producto = buscar_producto(inventario, codigo)
    if producto:
        producto["stock"] = nueva_cantidad
        print(f"Stock actualizado para {producto['nombre']}: {nueva_cantidad}")
    else:
        print(f"No se encontró producto con código {codigo}")

def eliminar_producto(inventario, codigo):
    producto = buscar_producto(inventario, codigo)
    if producto:
        inventario.remove(producto)
        print(f"Producto con código {codigo} eliminado del inventario")
    else:
        print(f"No se encontró producto con código {codigo}")

print("\n--- Pruebas CRUD ---")

# Buscar producto
codigo_buscar = "P002"
encontrado = buscar_producto(inventario, codigo_buscar)
if encontrado:
    print(f"Producto encontrado: {encontrado['nombre']} con stock {encontrado['stock']}")
else:
    print(f"No se encontró producto con código {codigo_buscar}")

# Actualizar stock
actualizar_stock(inventario, "P003", 60)

# Eliminar producto
eliminar_producto(inventario, "P001")

print("\nInventario luego de actualizaciones:")
for producto in inventario:
    print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")
