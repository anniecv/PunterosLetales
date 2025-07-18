mis_notas = [85.5, 90, 78, 88.5, 95, 82]

suma_total = 0

for nota in mis_notas:
    suma_total += nota

promedio = suma_total / len(mis_notas)

print(f"Suma total de las notas: {suma_total}")
print(f"Promedio de las notas: {promedio:.2f}")

suma_esperada = sum(mis_notas)
promedio_esperado = suma_esperada / len(mis_notas)

assert suma_total == suma_esperada, f"Error: la suma debería ser {suma_esperada}"
assert promedio == promedio_esperado, f"Error: el promedio debería ser {promedio_esperado:.2f}"

print("OK. Todo correcto. Las validaciones pasaron exitosamente.")
