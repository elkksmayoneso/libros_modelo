class base_datos_libro_modelo:

    def __init__(self):
        self.base_datos_libro = []

    def append_libro(self, libro):
        self.base_datos_libro.append(libro)

    def extend_libros(self, lista):
        self.base_datos_libro.extend(lista)

    def insert_libro(self, pos, libro):
        self.base_datos_libro.insert(pos, libro)

    def remove_libro(self, libro):
        self.base_datos_libro.remove(libro)

    def pop_libro(self, pos):
        return self.base_datos_libro.pop(pos)

    def index_libro(self, libro):
        return self.base_datos_libro.index(libro)

    def count_libro(self, libro):
        return self.base_datos_libro.count(libro)

    def sort_libros(self):
        self.base_datos_libro.sort(key=lambda x: x.get_tematica())

    def reverse_libros(self):
        self.base_datos_libro.reverse()

    def mostrar_libros(self):
        for libro in self.base_datos_libro:
            print(
                f"{libro.get_tematica()} - {libro.get_fecha()} - {libro.get_cantidad_hojas()}"
            )
