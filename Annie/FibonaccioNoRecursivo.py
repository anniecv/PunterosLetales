#Funcion para generar una secuencia de Fibonacci no recursiva
def fibonacci(n):
    if n <= 0:
        # Si el numero no es positivo, se lanza un error
        raise ValueError("El numero debe ser positivo.")
    elif n == 1:
        return [0]  # Primer numero de Fibonacci
    elif n == 2:
        return [0, 1]  # Primeros dos numeros de Fibonacci

    # Lista que contiene los primeros dos elementos iniciales
    fib_seq = [0, 1]

    # Desde el tercero hasta el enesimo, se calcula como suma de los dos anteriores
    for i in range(2, n):
        siguiente = fib_seq[i - 1] + fib_seq[i - 2]
        fib_seq.append(siguiente)

    return fib_seq

# Funcion que muestra la secuencia generada
def mostrar_fibonacci(n):
    try:
        secuencia = fibonacci(n)
        print(f"Los primeros {n} numeros de Fibonacci son:")
        print(secuencia)
    except ValueError as e:
        print(e)

# --- Ejecucion interactiva ---
# Permite al usuario ingresar un numero y muestra la secuencia correspondiente
try:
    numero = int(input("Ingrese la cantidad de numeros Fibonacci que desea generar: "))
    mostrar_fibonacci(numero)
except ValueError:
    print("Entrada invalida. Por favor ingrese un numero entero valido.")

# --- Pruebas automáticas con assert ---
# Estas lineas verifican que la funcion fibonacci() funciona correctamente

# Caso base: solo un elemento
assert fibonacci(1) == [0], "Error: fibonacci(1) deberia devolver [0]"

# Caso base: dos elementos
assert fibonacci(2) == [0, 1], "Error: fibonacci(2) deberia devolver [0, 1]"

# Verificacion de una secuencia pequeña
assert fibonacci(5) == [0, 1, 1, 2, 3], "Error: fibonacci(5) deberia devolver [0, 1, 1, 2, 3]"

# Secuencia mas larga, verificacion completa
assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "Error: fibonacci(10) incorrecto"

# Verifica especificamente el valor del tercer numero
assert fibonacci(3)[-1] == 1, "Error: el tercer numero de Fibonacci deberia ser 1"
