def crear_sala(filas, columnas):
  sala = []
  for i in range(filas):
      fila = []
      for j in range(columnas):
          if 2 <= j <= 5:
              precio = 50
          else:
              precio = 30
          fila.append({"estado": "L", "precio": precio})
      sala.append(fila)
  return sala

def mostrar_sala(sala):
  print("\n     " + " ".join(f"{j:^5}" for j in range(len(sala[0]))))
  print("     " + " ".join("─" * 5 for _ in range(len(sala[0]))))
  for i, fila in enumerate(sala):
      estado_fila = " ".join(f"{a['estado']:^5}" for a in fila)
      print(f"F{i:>2} | {estado_fila}")

def ocupar_asiento(sala, fila, columna):
  if 0 <= fila < len(sala) and 0 <= columna < len(sala[0]):
      asiento = sala[fila][columna]
      if asiento["estado"] == "L":
          asiento["estado"] = "O"
          print(f"Asiento ({fila}, {columna}) reservado por Bs. {asiento['precio']}")
          return True
      else:
          print("Ese asiento ya está ocupado.")
          return False
  else:
      print("Coordenadas inválidas.")
      return False

def buscar_asientos_juntos(sala, cantidad):
  for i, fila in enumerate(sala):
      consecutivos = 0
      for j, asiento in enumerate(fila):
          if asiento["estado"] == "L":
              consecutivos += 1
              if consecutivos == cantidad:
                  return i, j - cantidad + 1
          else:
              consecutivos = 0
  return None, None

def ocupar_asientos_juntos(sala, cantidad):
  fila, inicio = buscar_asientos_juntos(sala, cantidad)
  if fila is not None:
      total = 0
      for j in range(inicio, inicio + cantidad):
          sala[fila][j]["estado"] = "O"
          total += sala[fila][j]["precio"]
      print(f"{cantidad} asientos reservados en fila {fila}, desde columna {inicio}.")
      print(f"Total a pagar: Bs. {total}")
      return True
  else:
      print("No hay suficientes asientos contiguos disponibles.")
      return False

def contar_asientos_libres(sala):
  return sum(asiento["estado"] == "L" for fila in sala for asiento in fila)

def main():
  filas, columnas = 5, 8
  sala = crear_sala(filas, columnas)

  while True:
      print("\nSala actual:")
      mostrar_sala(sala)
      print(f"Asientos libres: {contar_asientos_libres(sala)}")
      print("\nMenú:")
      print("1. Ocupar asiento individual")
      print("2. Buscar y ocupar N asientos juntos")
      print("0. Salir")

      opcion = input("Elige una opción: ")

      if opcion == '1':
          try:
              fila = int(input("Fila: "))
              columna = int(input("Columna: "))
              ocupar_asiento(sala, fila, columna)
          except ValueError:
              print("Entrada inválida.")
      elif opcion == '2':
          try:
              n = int(input("¿Cuántos asientos necesitas juntos?: "))
              ocupar_asientos_juntos(sala, n)
          except ValueError:
              print("Entrada inválida.")
      elif opcion == '0':
          print("Gracias por usar el sistema de reserva de cine.")
          break
      else:
          print("Opción no válida.")

if __name__ == "__main__":
  main()
