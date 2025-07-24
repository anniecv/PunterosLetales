import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # <-- cámbiala según tu configuración
        database="Proyectofinal"
    )

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)",
            (self.nombre, self.precio, self.stock)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

class Cliente:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO clientes (nombre, apellido, telefono) VALUES (%s, %s, %s)",
            (self.nombre, self.apellido, self.telefono)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

class Venta:
    def __init__(self, cliente_id, producto_id, cantidad):
        self.cliente_id = cliente_id
        self.producto_id = producto_id
        self.cantidad = cantidad

    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar si hay stock suficiente
        cursor.execute("SELECT stock FROM productos WHERE id = %s", (self.producto_id,))
        resultado = cursor.fetchone()
        if resultado is None:
            raise Exception("Producto no encontrado")
        stock_actual = resultado[0]
        if stock_actual < self.cantidad:
            raise Exception("Stock insuficiente")

        # Registrar venta
        cursor.execute(
            "INSERT INTO ventas (cliente_id, producto_id, cantidad) VALUES (%s, %s, %s)",
            (self.cliente_id, self.producto_id, self.cantidad)
        )

        # Actualizar stock del producto
        cursor.execute(
            "UPDATE productos SET stock = stock - %s WHERE id = %s",
            (self.cantidad, self.producto_id)
        )

        conexion.commit()
        conexion.close()
