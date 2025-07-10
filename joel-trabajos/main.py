from funciones import saludar,sumar,clasificacionPelicula,tablaMultiplicar
def main():
    saludo = input("Por favor, ingresa tu nombre : ")
    saludar(saludo)
    print("Vamos a realizar algunas operaciones básicas.")

    # Clasificación de películas
    edad = int(input("Por favor, ingresa tu edad: "))
    clasificacionPelicula(edad)

    # Sumar dos números
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    print("La suma es:", sumar(num1, num2))

    # Tabla de multiplicar
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    tablaMultiplicar(numero)
    print("--- Fin del programa --- Joel Trabajos ---")

main()