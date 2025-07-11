mis_Notas = [85.5, 90.0, 78.5, 88.0, 92.5]

suma_Total = 0

for nota in mis_Notas:
    suma_Total += nota

Promedio = suma_Total / len(mis_Notas)

print(f"La suma total de las notas es: {suma_Total}")
print(f"El promedio de las notas es: {Promedio:.2f}")


#validacion con pruebas assert

suma_Esperada = sum(mis_Notas)
Promedio_Esperado = suma_Esperada / len(mis_Notas)

assert suma_Total == suma_Esperada, "Error: La suma total no es correcta."
assert Promedio == Promedio_Esperado, "Error: El promedio no es correcto."

print("✅ Las pruebas se han pasado correctamente.")
# Fin del código