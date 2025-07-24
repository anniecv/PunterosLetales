class clsUsuario:
    def __init__(self):
        self.Nombre = None
        self.Apellido = None
        self.Usuario = None
        self.Contrasenia = None
        self.Estado = 0

    def CrearUsuario(self, pnombre, papellido, pusuario, pcontra):
        self.Nombre = pnombre
        self.Apellido = papellido
        self.Usuario = pusuario
        self.Contrasenia = pcontra
        self.Estado = 1

    def IniciarSesion(self, pusr, ppass):
        usuario2 = pusr
        password = ppass
        if (self.Usuario == usuario2):
            if (self.Contrasenia == password):
                return(2)
            else:
                return(1)
        else:
            return(0)
    def CerrarSesion(self):
        self.Nombre = None
        self.Apellido = None
        self.Usuario = None
        self.Contrasenia = None
        self.Estado = 1

    def cambiarContraseña(self, ppass, ppassNew):
        passwordActual = ppass
        if (passwordActual == self.Contrasenia):
            password = ppassNew
            self.Contrasenia = password
            return True
        else:
            return False

    def ActivarCuenta(self):
        if self.Estado == 0:
            self.Estado = 1
        else:
            self.Estado = 0