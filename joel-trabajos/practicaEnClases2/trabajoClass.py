import csv
datos = [{"nombre": "Ana", "edad": 20}, 
{"nombre": "Luis", "edad": 22}]
encabezados = ["nombre", "edad"]
# 'newline=""' es importante para evitar 
# líneas en blanco extra
with open("datos.csv", "w", newline="", 
encoding="utf-8") as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, 
fieldnames=encabezados)
    escritor.writeheader()  # Escribe la 
#fila de encabezados
    escritor.writerows(datos) # Escribe 
#todos los diccionario

lista_leida = []
with open("datos.csv", "r", newline="", 
encoding="utf-8") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila_dict in lector:
        # ¡Recordar convertir tipos!
        # fila_dict['edad'] = int(fila_dict['edad'])
        lista_leida.append(fila_dict)