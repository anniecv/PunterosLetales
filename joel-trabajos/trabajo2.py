def clasificacionPelicula(edad):
    if edad < 0:
        return "Edad no válida"
    elif edad < 13:
        return "Puede ver peliculas clasificadas G o PG"
    elif edad < 18:
        return "Puede ver peliculas clasificadas PG-13"
    else:
        return "Puede ver peliculas clasificadas R!"

# Pruebas
assert clasificacionPelicula(20) == "Puede ver peliculas clasificadas R!", "Error para edad 20"
assert clasificacionPelicula(15) == "Puede ver peliculas clasificadas PG-13", "Error para edad 15"
assert clasificacionPelicula(10) == "Puede ver peliculas clasificadas G o PG", "Error para edad 10"
assert clasificacionPelicula(-5) == "Edad no válida", "Error para edad -5"

print("Todas las pruebas pasaron exitosamente.")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        resultado = clasificacionPelicula(edad)
        print(resultado)
    except ValueError:
        print("Por favor, ingrese un número válido para la edad.")
        continue

    continuar = input("¿Desea ingresar otra edad? (s/n): ").strip().lower()
    if continuar != 's':
        print("Gracias por usar el programa.")
        break

print("fin del programa, gracias por usarlo.")
# Fin del código