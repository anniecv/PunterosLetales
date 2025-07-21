class Libro:

    def __init__(self, titulo, autor, isbn, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.disponible = True

    def mostrar_info(self):
        print("=" * 50)
        print("INFORMACIÓN DEL LIBRO")
        print("=" * 50)
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")
        print("=" * 50)


if __name__ == "__main__":
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 417)
    libro2 = Libro("1984", "George Orwell", "978-0451524935", 328)
    libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0156013987", 96)

    mi_biblioteca = []

    mi_biblioteca.append(libro1)
    mi_biblioteca.append(libro2)
    mi_biblioteca.append(libro3)

    print("\n\n--- INVENTARIO COMPLETO DE LA BIBLIOTECA ---")
    for libro_actual in mi_biblioteca:
        libro_actual.mostrar_info()
        print("=" * 20)