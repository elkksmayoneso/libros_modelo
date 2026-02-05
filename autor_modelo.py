class autor_modelo:
    def __init__(self, nombre, edad, estado_civil, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.estado_civil = estado_civil
        self.nacionalidad = nacionalidad
        
    def set_nombre_autor(self, nombre):
        self.nombre = nombre
    
    def set_edad_autor(self,edad):
        self.edad = edad
        
    def set_estado_civil(self,estado_civil):
        self.estado_civil = estado_civil
        
    def set_nacionalidad_civil(self,nacionalidad):
        self.nacionalidad = nacionalidad 
    
    def get_nombre_autor(self):
        return self.nombre
    
    def get_edad_autor(self):
        return self.edad
    
    def get_estado_civil(self):
        return self.estado_civil
    
    def get_nacionalidad(self):
        return self.nacionalidad
        
    def registrar_datos(self):
        mensaje = "se registraron nuevos datos"
        return mensaje
    
    def mostrar_info_autor(self):
        mensaje = "la informacion del autor es la siguiente: "
        mensaje = mensaje + self.get_nombre_autor + self.get_edad_autor + self.get_estado_civil + self.get_nacionalidad
    
    def buscar_autor(self,dato_buscar):
        mensaje = "autor existe en la base de datos" + dato_buscar
        return mensaje
    
    def dar_baja_autor (self,dato):
        mensaje="el autor esta inactivo" + dato
        return mensaje