class base_datos_libro_modelo:
    
    def __init__(self):
        self.base_datos_libro = []

    def guardar_libro(self, obj_libro):
        self.base_datos_libro.append(obj_libro)

    def extender_libros(self, nueva_lista):
        self.base_datos_libro.extend(nueva_lista)

    def insertar_libros(self, obj_libro, pos):
        self.base_datos_libro.insert(pos, obj_libro)

    def eliminar_libro(self, obj_libro):
        self.base_datos_libro.remove(obj_libro)

    def eliminar_por_pos_libro(self, obj_libro, pos):
        self.base_datos_libro.pop(pos, obj_libro)

    def buscar_libro(self, nombre_obj):
        self.base_datos_libro.index(nombre_obj)

    def contar_libro(self, valor):
        self.base_datos_libro.count(valor)

    def ordenar_libros(self):
        self.base_datos_libro.sort()

    def invertir_libros(self):
        self.base_datos_libro.reverse()

    def mostrar_info_libro(self):
        for i in range(len(self.base_datos_libro)):
            tematica = self.base_datos_libro[i].get_tematica()
            fecha = self.base_datos_libro[i].get_fecha()
            cantidad_hojas = self.base_datos_libro[i].get_cantidad_hojas()

            print (f"Tematica libro: {tematica}, Fecha libro: {fecha}, Cantidad de hojas:  {cantidad_hojas}" )