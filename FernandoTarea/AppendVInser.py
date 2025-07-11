# Creamos una lista vacía
numeros = []

# append agrega al final
numeros.append(50)
numeros.append(40)
print("Usando append:", numeros)  # [10, 20]

# insert agrega en una posición específica
numeros.insert(1, 15)  # insertar en índice 1 el valor 15
print("Usando insert:", numeros)  # [10, 15, 20]

# Reemplazamos la lista 'numeros' con nuevos valores
numeros = [1, 2, 3, 4]

# Queremos multiplicar cada número por 5.5
duplicados = list(map(lambda x: x * 5.5, numeros))
print("Usando map:", duplicados)  # [5.5, 11.0, 16.5, 22.0]
