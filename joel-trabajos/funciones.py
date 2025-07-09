def saludar(saludo):
    print("hola " + saludo + " bienvenido a tu primer trabajo")

def clasificacionPelicula(edad):
    if edad < 0:
        return "Edad no válida"
    elif edad < 13:
        return "Puede ver peliculas clasificadas G o PG"
    elif edad < 18:
        return "Puede ver peliculas clasificadas PG-13"
    else:
        return "Puede ver peliculas clasificadas R!"

def sumar(a, b):
    return a + b

def tablaMultiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")