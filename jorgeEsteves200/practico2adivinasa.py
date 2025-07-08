
import random

numero_secreto = random.randint(1, 100)
num_azar = int(input("Ingresa un número al azar entre 1 y 100: "))

while num_azar != numero_secreto:
    if num_azar < numero_secreto:
        print("El número que ingresaste es menor al número secreto.")
    else:
        print("El número que ingresaste es mayor al número secreto.")

    num_azar = int(input("Intenta de nuevo. Ingresa otro número: "))

print("¡Felicidades! Adivinaste el número.")