def serie_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Ejemplo: imprimir los primeros 10 términos
print("Serie de Fibonacci (10 términos):")
serie_fibonacci(10)
