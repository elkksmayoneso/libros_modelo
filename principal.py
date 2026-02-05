from Libro_modelo import Libro_modelo
from autor_modelo import autor_modelo
from base_datos_libro_modelo import base_datos_libro_modelo
from api_datos_autores import api_datos_autores

obj_api_autores = api_datos_autores()
lista_autores = ["juan", "33", "casado", "colombiano"]
obj_bd_libro = base_datos_libro_modelo()

obj_api_autores.guardar_autores(lista_autores)

obj_autor = autor_modelo("juan", "33", "casado", "colombiano")

obj_libro1 = Libro_modelo("3 de febrero","650","ficcion")
obj_libro2 = Libro_modelo("6 de febrero","125","drama")
obj_libro3 = Libro_modelo("9 de febrero","289","romance")
obj_libro4 = Libro_modelo("12 de febrero","453","ficcion")

obj_bd_libro.guardar_libro(obj_libro1)
obj_bd_libro.guardar_libro(obj_libro2)
obj_bd_libro.guardar_libro(obj_libro3)
obj_bd_libro.guardar_libro(obj_libro4)

obj_bd_libro.mostrar_info_libro()