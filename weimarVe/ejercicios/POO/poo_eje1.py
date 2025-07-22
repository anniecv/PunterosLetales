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
    libro1.mostrar_info()

    libro1.disponible = False
    print("\nDespués de cambiar disponibilidad:")
    libro1.mostrar_info()