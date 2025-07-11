def fibonacci_recursivo(n):
    # Funcion que devuelve el enesimo numero de Fibonacci
    if n <= 0:
        raise ValueError("El numero debe ser positivo.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def generar_lista_fibonacci(n):
    # Devuelve una lista con los primeros n numeros de Fibonacci
    if n <= 0:
        raise ValueError("El numero debe ser positivo.")
    
    lista = []
    for i in range(1, n + 1):
        lista.append(fibonacci_recursivo(i))
    return lista

def mostrar_fibonacci(n):
    try:
        secuencia = generar_lista_fibonacci(n)
        print(f"Los primeros {n} numeros de Fibonacci son:")
        print(secuencia)
    except ValueError as e:
        print(e)

# --- Ejecucion interactiva ---
try:
    numero = int(input("Ingrese la cantidad de numeros Fibonacci que desea generar: "))
    mostrar_fibonacci(numero)
except ValueError:
    print("Entrada invalida. Por favor ingrese un numero entero valido.")
