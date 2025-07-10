def verificar_adivinanza(numero_secreto, intento):
  """Devuelve una pista segÃºn la diferencia entre el intento y el nÃºmero secreto."""
  if intento < numero_secreto:
      return "Demasiado bajo"
  elif intento > numero_secreto:
      return "Demasiado alto"
  else:
      return "Correcto"

# ====== Pruebas unitarias ======
assert verificar_adivinanza(7, 3) == "Demasiado bajo", "Error: se esperaba 'Demasiado bajo'"
assert verificar_adivinanza(7, 10) == "Demasiado alto", "Error: se esperaba 'Demasiado alto'"
assert verificar_adivinanza(7, 7) == "Correcto", "Error: se esperaba 'Correcto'"

print("âœ… Pruebas unitarias superadas.")

# ====== Juego interactivo ======
numero_secreto = 7
print("ðŸ” Adivina el nÃºmero secreto entre 1 y 10.")

while True:
  try:
      intento = int(input("Ingresa tu nÃºmero: "))
      resultado = verificar_adivinanza(numero_secreto, intento)

      if resultado == "Correcto":
          print(f"ðŸŽ‰ Â¡Correcto! El nÃºmero era {numero_secreto}.")
          break
      else:
          print(f"âŒ {resultado}. Intenta de nuevo.")
  except ValueError:
      print("âš ï¸ Por favor, ingresa un nÃºmero vÃ¡lido.")