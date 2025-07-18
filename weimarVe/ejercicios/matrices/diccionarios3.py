# 1. Uso de .keys(): Obtener todas las claves
producto = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor": "El Ceibo Ltda."
}

print("Claves del diccionario producto:")
for clave in producto.keys():
    print(f"→ {clave}")

# 2. Uso de .values(): Obtener todos los valores
print("\nValores del diccionario producto:")
for valor in producto.values():
    print(f"→ {valor}")

# 3. Uso de .items(): Recorrer clave y valor al mismo tiempo
print("\nContenido completo del diccionario producto:")
for clave, valor in producto.items():
    print(f"{clave}: {valor}")

# 4. Verificar si una clave existe usando 'in'
clave_a_verificar = "en_oferta"

if clave_a_verificar in producto:
    print(f"\n🔍 La clave '{clave_a_verificar}' existe con valor: {producto[clave_a_verificar]}")
else:
    print(f"\n❌ La clave '{clave_a_verificar}' no existe.")

if "stock" in producto:
    print(f"Stock disponible: {producto['stock']} unidades")
else:
    print("No hay información de stock.")

# Aplicado al inventario con .items()
inventario = [
    {"nombre": "Chocolate para Taza 'El Ceibo'", "stock": 50},
    {"nombre": "Café de los Yungas", "stock": 100},
    {"nombre": "Quinua Real en Grano", "stock": 80}
]

print("\n--- Detalle de productos usando .items() ---")
for producto in inventario:
    for clave, valor in producto.items():
        print(f"{clave} → {valor}")
    print("---")

# Modelado de datos con diccionarios para Canción
cancion = {
    "titulo": "Bohemian Rhapsody",
    "artista": "Queen",
    "album": "A Night at the Opera",
    "duracion_segundos": 354,
    "genero": "Rock Progresivo",
    "es_explicita": False,
    "reproducciones": 275_000_000
}

print("\n🎵 Canción:")
for clave, valor in cancion.items():
    print(f"{clave}: {valor}")

# Modelado de datos con diccionarios para Coche
coche = {
    "marca": "Toyota",
    "modelo": "Corolla Cross",
    "año": 2023,
    "color": "Gris Metálico",
    "placa": "5923-LLT",
    "kilometraje": 17450.6,
    "en_venta": True
}

print("\n🚗 Coche:")
for clave, valor in coche.items():
    print(f"{clave}: {valor}")

# Modelado de datos con diccionarios para Post de Red Social
post_red_social = {
    "id_post": "POST-20250622-001",
    "autor": "weimar.valda",
    "contenido_texto": "¡Hoy lanzamos nuestro nuevo ERP con IA! 🚀",
    "lista_de_likes": ["ana_123", "dev.mario", "claudia77"],
    "fecha_publicacion": "2025-06-22",
    "es_publico": True,
    "hashtags": ["#IA", "#ERP", "#ProductLaunch"]
}

print("\n📱 Post en Red Social:")
for clave, valor in post_red_social.items():
    print(f"{clave}: {valor}")

# Verificar existencia de clave
if "autor" in post_red_social:
    print(f"\n✅ Autor del post: {post_red_social['autor']}")
else:
    print("❌ Este post no tiene autor definido.") no