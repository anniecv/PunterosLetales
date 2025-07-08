import random

numero_secreto = random.randint(1, 10)
intento = None

print("Adivina el número entre 1 y 10")

while intento != numero_secreto:
    intento = int(input("Tu número: "))

    if intento < numero_secreto:
        print("¡Muy bajo!")
    elif intento > numero_secreto:
        print("¡Muy alto!")
    else: print("Yuupi adivinastee ")
