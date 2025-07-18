from getpass import getpass

print (" un juego iterativo entre 2 personas unete con tu amigo y adivina la lista secreta")
print ("debes descubrir que numeros hay en la lista secreta de 5 elementos dada por tu amigo separadas por comas")
print ("paso 1 tu amigo pone la lista secreta")
print ("ingresa la lista secreta separada por comas")
print ("tienes 3 intentos para adivinar la lista secreta")
print (" veras tu progrso en la lista con los 3 intentos")

print (".----------------------------------------------------------------------.")
lista_secreta_str = getpass("Amigo, ingresa la lista secreta separada por comas (ej: 1,2,3,4,5): ")
try:
    lista_secreta = [int(x.strip()) for x in lista_secreta_str.split(",")]
    if len(lista_secreta) != 5:
        print("La lista debe tener exactamente 5 elementos.")
        exit()
except ValueError:
    print("Error: la lista debe contener solo números enteros separados por comas.")
    exit()
print("¡Ahora es tu turno de adivinar la lista secreta!")
intentos = 3
historial = []