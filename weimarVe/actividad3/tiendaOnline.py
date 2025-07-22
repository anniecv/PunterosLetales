import json
import os
from datetime import datetime

# Sistema de archivos para persistencia
PRODUCTOS_FILE = "productos.json"
CLIENTES_FILE = "clientes.json"
PEDIDOS_FILE = "pedidos.json"

class Producto:
    def __init__(self, id, nombre, precio, stock, categoria="General"):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def mostrar_info(self):
        return f"[{self.id}] {self.nombre} - ${self.precio:.2f} | Stock: {self.stock} | Categoría: {self.categoria}"

    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje/100)

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "categoria": self.categoria
        }

class Cliente:
    def __init__(self, id, nombre, email, direccion):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.carrito = CarritoDeCompras()
        self.historial = []

    def ver_carrito(self):
        return self.carrito.mostrar_carrito()

    def realizar_compra(self):
        if not self.carrito.items:
            return False, "❌ No hay productos en el carrito"

        # Verificar stock
        for item in self.carrito.items:
            producto, cantidad = item
            if cantidad > producto.stock:
                return False, f"❌ Stock insuficiente para {producto.nombre} (Stock: {producto.stock})"

        # Crear pedido
        total = self.carrito.calcular_total()
        pedido = Pedido(
            id=len(self.historial) + 1,
            cliente=self,
            items=self.carrito.items.copy(),
            total=total
        )

        # Actualizar stock
        for item in self.carrito.items:
            producto, cantidad = item
            producto.actualizar_stock(-cantidad)

        # Guardar en historial
        self.historial.append(pedido)
        self.carrito.vaciar_carrito()

        return True, f"🎉 Compra realizada! ID Pedido: {pedido.id} | Total: ${total:.2f}"

    def ver_historial(self):
        if not self.historial:
            return "📜 No hay compras registradas"

        reporte = f"\n📜 Historial de compras de {self.nombre}:\n"
        for pedido in self.historial:
            reporte += f"\n{pedido.mostrar_info()}\n"
        return reporte

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "direccion": self.direccion,
            "carrito": self.carrito.to_dict(),
            "historial": [pedido.to_dict() for pedido in self.historial]
        }

class CarritoDeCompras:
    def __init__(self):
        self.items = []  # [(producto, cantidad)]

    def agregar_producto(self, producto, cantidad=1):
        # Buscar si ya está en el carrito
        for i, (prod, cant) in enumerate(self.items):
            if prod.id == producto.id:
                self.items[i] = (prod, cant + cantidad)
                return f"➕ {cantidad} unidad(es) de {producto.nombre} añadidas al carrito"

        # Si no está, añadirlo
        self.items.append((producto, cantidad))
        return f"🛒 {cantidad} unidad(es) de {producto.nombre} añadidas al carrito"

    def remover_producto(self, producto_id):
        for i, (prod, cantidad) in enumerate(self.items):
            if prod.id == producto_id:
                nombre = prod.nombre
                del self.items[i]
                return f"➖ {nombre} removido del carrito"
        return "❌ Producto no encontrado en el carrito"

    def actualizar_cantidad(self, producto_id, nueva_cantidad):
        for i, (prod, cantidad) in enumerate(self.items):
            if prod.id == producto_id:
                if nueva_cantidad <= 0:
                    return self.remover_producto(producto_id)
                self.items[i] = (prod, nueva_cantidad)
                return f"✏️ Cantidad de {prod.nombre} actualizada a {nueva_cantidad}"
        return "❌ Producto no encontrado en el carrito"

    def mostrar_carrito(self):
        if not self.items:
            return "🛒 Tu carrito está vacío"

        reporte = "🛒 Contenido del carrito:\n"
        total = 0
        for i, (producto, cantidad) in enumerate(self.items):
            subtotal = producto.precio * cantidad
            total += subtotal
            reporte += f"{i+1}. {producto.nombre} x {cantidad} = ${subtotal:.2f}\n"

        reporte += f"\n💲 Total: ${total:.2f}"
        return reporte

    def calcular_total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.items)

    def vaciar_carrito(self):
        self.items = []

    def to_dict(self):
        return [{"producto_id": producto.id, "cantidad": cantidad} 
                for producto, cantidad in self.items]

class Pedido:
    def __init__(self, id, cliente, items, total):
        self.id = id
        self.cliente = cliente
        self.items = items  # [(producto, cantidad)]
        self.total = total
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.estado = "Completado"

    def mostrar_info(self):
        info = f"📦 Pedido #{self.id} | Fecha: {self.fecha}\n"
        info += f"👤 Cliente: {self.cliente.nombre} | Total: ${self.total:.2f}\n"
        info += "Productos:\n"
        for producto, cantidad in self.items:
            info += f"- {producto.nombre} x {cantidad} (${producto.precio:.2f} c/u)\n"
        info += f"Estado: {self.estado}"
        return info

    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente.id,
            "items": [{"producto_id": producto.id, "cantidad": cantidad} 
                      for producto, cantidad in self.items],
            "total": self.total,
            "fecha": self.fecha,
            "estado": self.estado
        }

class TiendaOnline:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.cargar_datos()

    def cargar_datos(self):
        # Cargar productos
        if os.path.exists(PRODUCTOS_FILE):
            with open(PRODUCTOS_FILE, 'r') as f:
                datos = json.load(f)
                self.productos = [Producto(**p) for p in datos]

        # Cargar clientes
        if os.path.exists(CLIENTES_FILE):
            with open(CLIENTES_FILE, 'r') as f:
                clientes_data = json.load(f)
                for c in clientes_data:
                    cliente = Cliente(
                        id=c['id'],
                        nombre=c['nombre'],
                        email=c['email'],
                        direccion=c['direccion']
                    )

                    # Cargar carrito
                    for item in c['carrito']:
                        producto = self.buscar_producto_por_id(item['producto_id'])
                        if producto:
                            cliente.carrito.agregar_producto(producto, item['cantidad'])

                    # Cargar historial
                    for p in c['historial']:
                        items = []
                        for item in p['items']:
                            producto = self.buscar_producto_por_id(item['producto_id'])
                            if producto:
                                items.append((producto, item['cantidad']))

                        pedido = Pedido(
                            id=p['id'],
                            cliente=cliente,
                            items=items,
                            total=p['total']
                        )
                        pedido.fecha = p['fecha']
                        pedido.estado = p['estado']
                        cliente.historial.append(pedido)

                    self.clientes.append(cliente)

    def guardar_datos(self):
        # Guardar productos
        with open(PRODUCTOS_FILE, 'w') as f:
            json.dump([p.to_dict() for p in self.productos], f, indent=2)

        # Guardar clientes
        with open(CLIENTES_FILE, 'w') as f:
            json.dump([c.to_dict() for c in self.clientes], f, indent=2)

    def buscar_producto_por_id(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        return None

    def buscar_cliente_por_email(self, email):
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente
        return None

    def registrar_producto(self):
        print("\n📦 Registrar Nuevo Producto")
        id = input("ID del producto: ")
        if any(p.id == id for p in self.productos):
            print("❌ Ya existe un producto con ese ID")
            return

        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        categoria = input("Categoría: ")

        nuevo_producto = Producto(id, nombre, precio, stock, categoria)
        self.productos.append(nuevo_producto)
        self.guardar_datos()
        print(f"✅ Producto '{nombre}' registrado exitosamente!")

    def registrar_cliente(self):
        print("\n👤 Registrar Nuevo Cliente")
        id = input("ID del cliente: ")
        if any(c.id == id for c in self.clientes):
            print("❌ Ya existe un cliente con ese ID")
            return

        nombre = input("Nombre completo: ")
        email = input("Email: ")
        if self.buscar_cliente_por_email(email):
            print("❌ Ya existe un cliente con ese email")
            return

        direccion = input("Dirección de envío: ")

        nuevo_cliente = Cliente(id, nombre, email, direccion)
        self.clientes.append(nuevo_cliente)
        self.guardar_datos()
        print(f"✅ Cliente '{nombre}' registrado exitosamente!")

    def menu_cliente(self, cliente):
        while True:
            print("\n" + "="*50)
            print(f"👤 Bienvenido(a), {cliente.nombre}")
            print("1. Ver catálogo de productos")
            print("2. Buscar producto")
            print("3. Ver carrito")
            print("4. Agregar producto al carrito")
            print("5. Remover producto del carrito")
            print("6. Actualizar cantidad en carrito")
            print("7. Realizar compra")
            print("8. Ver historial de compras")
            print("9. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("\n📦 Catálogo de Productos:")
                for producto in self.productos:
                    print(producto.mostrar_info())

            elif opcion == "2":
                termino = input("Buscar producto (nombre o categoría): ").lower()
                resultados = [p for p in self.productos 
                             if termino in p.nombre.lower() or termino in p.categoria.lower()]

                if resultados:
                    print("\n🔍 Resultados de búsqueda:")
                    for producto in resultados:
                        print(producto.mostrar_info())
                else:
                    print("❌ No se encontraron productos")

            elif opcion == "3":
                print("\n" + cliente.ver_carrito())

            elif opcion == "4":
                id_producto = input("ID del producto a agregar: ")
                producto = self.buscar_producto_por_id(id_producto)

                if producto:
                    cantidad = int(input("Cantidad: ") or "1")
                    print(cliente.carrito.agregar_producto(producto, cantidad))
                    self.guardar_datos()
                else:
                    print("❌ Producto no encontrado")

            elif opcion == "5":
                id_producto = input("ID del producto a remover: ")
                print(cliente.carrito.remover_producto(id_producto))
                self.guardar_datos()

            elif opcion == "6":
                id_producto = input("ID del producto: ")
                nueva_cantidad = int(input("Nueva cantidad: "))
                print(cliente.carrito.actualizar_cantidad(id_producto, nueva_cantidad))
                self.guardar_datos()

            elif opcion == "7":
                exito, mensaje = cliente.realizar_compra()
                print("\n" + mensaje)
                if exito:
                    self.guardar_datos()

            elif opcion == "8":
                print(cliente.ver_historial())

            elif opcion == "9":
                print("👋 Sesión cerrada")
                break

            else:
                print("❌ Opción inválida")

    def iniciar(self):
        while True:
            print("\n" + "="*50)
            print("🛍️  TIENDA ONLINE - MENÚ PRINCIPAL")
            print("1. Iniciar sesión")
            print("2. Registrarse como nuevo cliente")
            print("3. Administrar productos (Registrar nuevo)")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                email = input("Email: ")
                cliente = self.buscar_cliente_por_email(email)
                if cliente:
                    self.menu_cliente(cliente)
                else:
                    print("❌ Cliente no encontrado")

            elif opcion == "2":
                self.registrar_cliente()

            elif opcion == "3":
                self.registrar_producto()

            elif opcion == "4":
                print("¡Gracias por usar nuestra tienda online!")
                break

            else:
                print("❌ Opción inválida")

# Iniciar la tienda
if __name__ == "__main__":
    tienda = TiendaOnline()
    tienda.iniciar()