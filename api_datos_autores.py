class api_datos_autores:

    def __init__(self):
        self.api_lista_autores = []

    # append()
    def append_autor(self, autor):
        self.api_lista_autores.append(autor)

    # extend()
    def extend_autores(self, lista_autores):
        self.api_lista_autores.extend(lista_autores)

    # insert()
    def insert_autor(self, pos, autor):
        self.api_lista_autores.insert(pos, autor)

    # remove()
    def remove_autor(self, autor):
        self.api_lista_autores.remove(autor)

    # pop()
    def pop_autor(self, pos):
        return self.api_lista_autores.pop(pos)

    # index()
    def index_autor(self, autor):
        return self.api_lista_autores.index(autor)

    # count()
    def count_autor(self, autor):
        return self.api_lista_autores.count(autor)

    # sort()
    def sort_autores(self):
        self.api_lista_autores.sort(
            key=lambda autor: autor.get_nombre_autor()
        )

    def buscar_autor_por_nombre(self, nombre):
        for autor in self.api_lista_autores:
            if autor.get_nombre_autor().lower() == nombre.lower():
                return autor
        return None

    # reverse()
    def reverse_autores(self):
        self.api_lista_autores.reverse()

    # mostrar
    def mostrar_autores(self):
        print("\n--- AUTORES REGISTRADOS ---")

        for autor in self.api_lista_autores:
            print(
                f"\nNombre: {autor.get_nombre_autor()}"
                f"\nEdad: {autor.get_edad_autor()}"
                f"\nEstado civil: {autor.get_estado_civil()}"
                f"\nNacionalidad: {autor.get_nacionalidad()}"
            )

            print("Libros:")
            if autor.get_libros():
                for libro in autor.get_libros():
                    print(
                        f"  - {libro.get_tematica()} | "
                        f"{libro.get_fecha()} | "
                        f"{libro.get_cantidad_hojas()} hojas"
                    )
            else:
                print("  (Sin libros registrados)")

