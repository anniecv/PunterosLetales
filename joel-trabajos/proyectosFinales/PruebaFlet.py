import flet as ft
import clsUsuario as p
objClsUsuario=p.clsUsuario

textNombre = ft.TextField(
        color="black", 
        width=200, 
        label="Ingrse su nombre ", 
        icon=ft.Icons.VERIFIED_USER, 
        border="underline",
        visible=False)

textApellido = ft.TextField(
        color="black", 
        width=200, 
        label="Ingrse su Apellido ", 
        icon=ft.Icons.VERIFIED_USER_OUTLINED, 
        border="underline",
        visible=False)

textUsuario = ft.TextField(
        color="black", 
        width=200, 
        label="Ingrse su Usuario ", 
        icon=ft.Icons.VERIFIED_USER, 
        border="underline", 
        text_size=20)

textPassword = ft.TextField(
        color="black", 
        width=200, 
        label="Ingrse su Password ", 
        icon=ft.Icons.LOCK, 
        border="underline", 
        password=True, 
        can_reveal_password=True,
        max_length=8)

btnCrear = ft.ElevatedButton(text="Crear Usuario")
btnIniciar = ft.ElevatedButton(text="Iniciar session")
IblMensaje =ft.Text(value="mensaje..", color="#FFC0CB",size=30)
btnGuardar = ft.TextButton(text="guardar datos")
principal = ft.Container(ft.Column([textNombre,textApellido,textUsuario,
                                    textPassword,btnCrear,btnIniciar,btnGuardar,IblMensaje]),
                                    width=400,
                                    height=500,
                                    padding=100,
                                    border_radius=50,
                                    gradient=ft.LinearGradient(
                                    colors=["#FF7003", "#B2FFBF", "#05EA2C"]
                                    )
                                    
)
def main(hoja: ft.Page):
    hoja.bgcolor="WHITE"
    def CrearUsuario(e):
        textNombre.visible=True
        textApellido.visible=True
        btnIniciar.visible=False
        btnCrear.visible=False
        btnGuardar.visible=True
        
        hoja.update()

    def GuardarDatos(e):
        objClsUsuario.CrearUsuario(objClsUsuario,textNombre.value,textApellido.value,textUsuario.value,textPassword.value)
        IblMensaje.value="usuario creado"

        textNombre.visible=False
        textNombre.value=""
        textApellido.visible=False 
        textApellido.value=None
        btnIniciar.visible=True
        btnCrear.visible=True
        btnGuardar.visible=False
        textUsuario.value=""
        textPassword.value=""
        hoja.update()


    btnCrear.on_click=CrearUsuario
    btnGuardar.on_click=GuardarDatos
    
    hoja.vertical_alignment="center"
    hoja.horizontal_alignment="center"

    hoja.add(principal)
ft.app(main)