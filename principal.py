from Libro_modelo import Libro_modelo
from autor_modelo import autor_modelo
from base_datos_libro_modelo import base_datos_libro_modelo
from api_datos_autores import api_datos_autores

bd_autores = api_datos_autores()
bd_libros = base_datos_libro_modelo()

def crear_autor_desde_input():
    nombre = input("Nombre del autor: ")
    edad = input("Edad: ")
    estado_civil = input("Estado civil: ")
    nacionalidad = input("Nacionalidad: ")
    return autor_modelo(nombre, edad, estado_civil, nacionalidad)

#El menu lo uso para comprobar los metodos del array

def menu():
    print("\n========= MENÚ PRINCIPAL =========")
    print("1. Agregar un autor (ingresando datos)")
    print("2. Agregar varios autores")
    print("3. Insertar autor en una posición")
    print("4. Eliminar autor por nombre")
    print("5. Eliminar autor por posición")
    print("6. Buscar posición de un autor por nombre")
    print("7. Contar cuántas veces aparece un autor")
    print("8. Mostrar autores")
    print("9. Invertir orden de la lista")
    print("10. Agregar un libro a un autor")
    print("0. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    match opcion:

        case "1":
            autor = crear_autor_desde_input()
            bd_autores.append_autor(autor)
            print("Autor agregado correctamente.")
            bd_autores.mostrar_autores()

        case "2":
            cantidad = int(input("¿Cuántos autores desea ingresar?: "))
            lista = []

            for i in range(cantidad):
                print(f"\nAutor #{i+1}")
                lista.append(crear_autor_desde_input())

            bd_autores.extend_autores(lista)
            print("Autores agregados correctamente.")
            bd_autores.mostrar_autores()

        case "3":
            pos = int(input("Ingrese la posición donde desea insertar el autor: "))
            autor = crear_autor_desde_input()
            bd_autores.insert_autor(pos, autor)
            print("Autor insertado correctamente.")
            bd_autores.mostrar_autores()

        case "4":
            nombre = input("Ingrese el nombre del autor a eliminar: ")
            autor = bd_autores.buscar_autor_por_nombre(nombre)

            if autor:
                bd_autores.remove_autor(autor)
                print("Autor eliminado correctamente.")
            else:
                print("Autor no encontrado.")

            bd_autores.mostrar_autores()

        case "5":
            pos = int(input("Ingrese la posición del autor a eliminar: "))
            try:
                eliminado = bd_autores.pop_autor(pos)
                print("Autor eliminado:", eliminado.get_nombre_autor())
            except IndexError:
                print("Posición inválida.")

            bd_autores.mostrar_autores()

        case "6":
            nombre = input("Ingrese el nombre del autor a buscar: ")
            autor = bd_autores.buscar_autor_por_nombre(nombre)

            if autor:
                pos = bd_autores.index_autor(autor)
                print(f"El autor '{nombre}' está en la posición {pos}.")
            else:
                print("Autor no encontrado.")

        case "7":
            nombre = input("Ingrese el nombre del autor a contar: ")
            autor = bd_autores.buscar_autor_por_nombre(nombre)

            if autor:
                cantidad = bd_autores.count_autor(autor)
                print(f"El autor '{nombre}' aparece {cantidad} veces.")
            else:
                print("Autor no encontrado.")

        case "8":
            bd_autores.mostrar_autores()

        case "9":
            bd_autores.reverse_autores()
            print("Lista de autores invertida.")
            bd_autores.mostrar_autores()

        case "10":
            if not bd_autores.api_lista_autores:
                print("No hay autores registrados.")
            else:
                nombre_autor = input("Ingrese el nombre del autor: ")
                autor = bd_autores.buscar_autor_por_nombre(nombre_autor)

            if autor:
                fecha = input("Fecha del libro: ")
                cantidad_hojas = input("Cantidad de hojas: ")
                tematica = input("Temática del libro: ")

                libro = Libro_modelo(fecha, cantidad_hojas, tematica)
                autor.agregar_libro(libro)

                print(f"Libro agregado correctamente al autor {autor.get_nombre_autor()}.")
                bd_autores.mostrar_autores()
            else:
                print("Autor no encontrado.")
        
        case "0":
            print("Saliendo del sistema...")
            break

        case _:
            print("Opción inválida.")
