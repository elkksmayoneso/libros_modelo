class autor_modelo:

    def __init__(self, nombre, edad, estado_civil, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.estado_civil = estado_civil
        self.nacionalidad = nacionalidad
        self.libros = []

    # getters
    def get_nombre_autor(self):
        return self.nombre

    def get_edad_autor(self):
        return self.edad

    def get_estado_civil(self):
        return self.estado_civil

    def get_nacionalidad(self):
        return self.nacionalidad

    def get_libros(self):
        return self.libros
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        
    def agregar_libro(self, libro):
        self.libros.append(libro)

    def get_libros(self):
        return self.libros

