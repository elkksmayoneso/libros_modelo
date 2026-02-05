class Libro_modelo:
    def __init__(self, fecha, cantidad_hojas, tematica):
        self.fecha = fecha
        self.cantidad_hojas = cantidad_hojas
        self.tematica = tematica
        
    def get_cantidad_hojas(self):
        return self.cantidad_hojas

    def get_tematica(self):
        return self.tematica
    
    def get_fecha(self):
        return self.fecha
        
#Hacer las responsabilidades de la clase

    def registrar_cantidad_hojas(self):
        mensaje = "se registraron en la base de datos"
        return mensaje

    def registrar_fecha_libro(self):
        mensaje = "Las fechas se registraron en la bd"
        return mensaje

    def mostrar_cantidad_hojas(self):
        mensaje = "el libro tiene la siguiente cantidad: "
        mensaje = mensaje + self.get_cantidad_hojas()
        return mensaje
    
    def registrar_tematica(self):
        mensaje = "tematica registrada"
        return mensaje
    
    def mostrar_tematica(self):
        mensaje=self.get_tematica
        return mensaje
    
    def ver_info_autor(self,obj_autor):
        obj_autor.mostrar_info_autor()