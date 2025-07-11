def calcular_area_rectangulo(base, altura):
  """Calcula el área de un rectángulo."""
  return base * altura

def mostrar_area_rectangulo(numero, base, altura):
  """Muestra el área de un rectángulo con formato."""
  area = calcular_area_rectangulo(base, altura)
  print(f"El área del rectángulo {numero} ({base}x{altura}) es: {area}")

def main():
  """Función principal del programa."""
  mostrar_area_rectangulo(1, 10, 5)
  mostrar_area_rectangulo(2, 8, 3)
  mostrar_area_rectangulo(3, 15, 7)

if __name__ == "__main__":
  main()
