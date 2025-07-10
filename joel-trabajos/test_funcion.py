from funciones import saludar,sumar,clasificacionPelicula
# Pruebas unitarias para la función clasificacionPelicula
assert saludar("Joel") == None, "Error en la función saludar"
assert saludar("Marta") == None, "Error en la función saludar con otro nombre"
assert saludar("Ana") == None, "Error en la función saludar con nombre Ana"
assert clasificacionPelicula(20) == "Puede ver peliculas clasificadas R!", "Error para edad 20"
assert clasificacionPelicula(15) == "Puede ver peliculas clasificadas PG-13", "Error para edad 15"
assert clasificacionPelicula(10) == "Puede ver peliculas clasificadas G o PG", "Error para edad 10"
assert clasificacionPelicula(-5) == "Edad no válida", "Error para edad -5"
assert sumar(5, 3) == 8, "Error en la suma de 5 y 3"
assert sumar(-1, 1) == 0, "Error en la suma de -1 y 1"
assert sumar(0, 0) == 0, "Error en la suma de 0 y 0"

print("Todas las pruebas pasaron exitosamente.")

