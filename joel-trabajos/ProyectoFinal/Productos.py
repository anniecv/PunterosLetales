import flet as ft
from modelo import Producto, Cliente, Venta

class VentanaClientes(ft.Column):
    def __init__(self):
        super().__init__()
        self.txt_nombre = ft.TextField(label="Nombre")
        self.txt_apellido = ft.TextField(label="Apellido")
        self.txt_telefono = ft.TextField(label="Teléfono")
        btn_agregar = ft.ElevatedButton("Agregar", on_click=self.agregar_cliente)

        self.lista_clientes = ft.Column(spacing=5, scroll=ft.ScrollMode.ALWAYS)

        super().controls.extend([
            ft.Text("Gestión de Clientes", size=24, weight="bold"),
            ft.Row([
                self.txt_nombre,
                self.txt_apellido,
                self.txt_telefono,
                btn_agregar
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(),
            ft.Text("Lista de clientes:"),
            self.lista_clientes
        ])

        self.cargar_clientes()

    def cargar_clientes(self):
        self.lista_clientes.controls.clear()
        clientes = Cliente.obtener_todos()
        for c in clientes:
            fila = ft.Row([
                ft.Text(str(c['id']), width=50),
                ft.Text(c['nombre'], width=150),
                ft.Text(c['apellido'], width=150),
                ft.Text(c['telefono'], width=100)
            ])
            self.lista_clientes.controls.append(fila)

    def agregar_cliente(self, e):
        try:
            nombre = self.txt_nombre.value
            apellido = self.txt_apellido.value
            telefono = self.txt_telefono.value

            cliente = Cliente(nombre, apellido, telefono)
            cliente.guardar()

            self.txt_nombre.value = ""
            self.txt_apellido.value = ""
            self.txt_telefono.value = ""

            self.cargar_clientes()
        except Exception as ex:
            print("Error al agregar cliente:", ex)

class VentanaProductos(ft.Column):
    def __init__(self):
        super().__init__()
        self.txt_nombre = ft.TextField(label="Nombre")
        self.txt_precio = ft.TextField(label="Precio")
        self.txt_stock = ft.TextField(label="Stock")
        btn_agregar = ft.ElevatedButton("Agregar", on_click=self.agregar_producto)

        self.lista_productos = ft.Column(spacing=5, scroll=ft.ScrollMode.ALWAYS)

        super().controls.extend([
            ft.Text("Gestión de Productos", size=24, weight="bold"),
            ft.Row([
                self.txt_nombre,
                self.txt_precio,
                self.txt_stock,
                btn_agregar
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(),
            ft.Text("Lista de productos:"),
            self.lista_productos
        ])

        self.cargar_productos()

    def cargar_productos(self):
        self.lista_productos.controls.clear()
        productos = Producto.obtener_todos()
        for p in productos:
            fila = ft.Row([
                ft.Text(str(p['id']), width=50),
                ft.Text(p['nombre'], width=150),
                ft.Text(str(p['precio']), width=100),
                ft.Text(str(p['stock']), width=100)
            ])
            self.lista_productos.controls.append(fila)

    def agregar_producto(self, e):
        try:
            nombre = self.txt_nombre.value
            precio = float(self.txt_precio.value)
            stock = int(self.txt_stock.value)

            producto = Producto(nombre, precio, stock)
            producto.guardar()

            self.txt_nombre.value = ""
            self.txt_precio.value = ""
            self.txt_stock.value = ""

            self.cargar_productos()
        except Exception as ex:
            print("Error al agregar producto:", ex)

class VentanaVentas(ft.Column):
    def __init__(self):
        super().__init__()
        self.txt_cliente_id = ft.TextField(label="ID Cliente")
        self.txt_producto_id = ft.TextField(label="ID Producto")
        self.txt_cantidad = ft.TextField(label="Cantidad")
        btn_vender = ft.ElevatedButton("Realizar Venta", on_click=self.realizar_venta)
        self.lbl_mensaje = ft.Text(value="")

        super().controls.extend([
            ft.Text("Registro de Ventas", size=24, weight="bold"),
            self.txt_cliente_id,
            self.txt_producto_id,
            self.txt_cantidad,
            btn_vender,
            self.lbl_mensaje
        ])

    def realizar_venta(self, e):
        try:
            cliente_id = int(self.txt_cliente_id.value)
            producto_id = int(self.txt_producto_id.value)
            cantidad = int(self.txt_cantidad.value)

            venta = Venta(cliente_id, producto_id, cantidad)
            venta.guardar()

            self.txt_cliente_id.value = ""
            self.txt_producto_id.value = ""
            self.txt_cantidad.value = ""

            self.lbl_mensaje.value = "Venta registrada exitosamente."
        except Exception as ex:
            self.lbl_mensaje.value = f"Error: {ex}"

if __name__ == "__main__":
    def main(pagina: ft.Page):
        pagina.title = "Sistema de Ventas"
        pagina.window_width = 800
        pagina.window_height = 600
        pagina.theme_mode = ft.ThemeMode.DARK

        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text="Productos", content=VentanaProductos()),
                ft.Tab(text="Clientes", content=VentanaClientes()),
                ft.Tab(text="Ventas", content=VentanaVentas()),
            ]
        )
        pagina.add(tabs)
    ft.app(target=main, view=ft.WEB_BROWSER)