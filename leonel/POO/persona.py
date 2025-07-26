# Persona
    #Tiene:
        # - nombre (texto)
        # - edad (numero entero)

# + bautizar()
# + saludar()
# + Cumplir_años()

class Persona:

    def bautizar(self, nombre, edad):
        self.nombre=nombre
        self.edad = edad

    def saludar(self):
        print("Hola me llamo", self.nombre, " y tengo ", self.edad)

    def cumplir_anios(self):
         self.edad = self.edad+1

persona1=Persona()
persona1.bautizar("Maria",25)
persona1.saludar()
persona1.cumplir_anios()
persona1.saludar()

persona2=Persona()
persona2.bautizar("Juan",15)
persona2.saludar()