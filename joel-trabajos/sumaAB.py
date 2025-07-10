def sumar(a, b):
    """
    Recibe dos números y devuelve su suma.
    """
    resultado_suma = a + b
    return resultado_suma

# ===== Pruebas unitarias con assert =====
assert sumar(2, 3) == 5, "Error: 2 + 3 debe ser 5"
assert sumar(-1, 1) == 0, "Error: -1 + 1 debe ser 0"
assert sumar(10, 0) == 10, "Error: 10 + 0 debe ser 10"
assert sumar(-5, -5) == -10, "Error: -5 + -5 debe ser -10"
assert sumar(100, 200) == 300, "Error: 100 + 200 debe ser 300"
# Prueba de suma con números grandes
assert sumar(1000000, 2000000) == 3000000, "Error: 1000000 + 2000000 debe ser 3000000"
# Prueba de suma con números negativos grandes
assert sumar(-1000000, -2000000) == -3000000, "Error: -1000000 + -2000000 debe ser -3000000"

print("✅ Pruebas unitarias para sumar() superadas.")
print("--- Fin del programa --- Joel Trabajos ---")
# Nota: Este código es un ejemplo de cómo se pueden realizar pruebas unitarias