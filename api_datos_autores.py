class api_datos_autores:

    def __init__(self):
        self.api_lista_autores = []

    def guardar_autores(self, lista_autores):
        self.api_lista_autores.append(lista_autores)
        print(self.api_lista_autores)

    def extender_autores(self, nueva_lista):
        self.api_lista_autores.extend(nueva_lista)

    def insertar_autor(self, lista_autores, pos):
        self.api_lista_autores.insert(pos, lista_autores)

    def eliminar_autor(self, lista_autores):
        self.api_lista_autores.remove(lista_autores)

    def eliminar_por_pos_autor(self, lista_autores, pos):
        self.api_lista_autores.pop(pos, lista_autores)

    def buscar_autor(self, nombre_obj):
        self.api_lista_autores.index(nombre_obj)

    def contar_autores(self, valor):
        self.api_lista_autores.count(valor)

    def ordenar_autores(self):
        self.api_lista_autores.sort()

    def invertir_autores(self):
        self.api_lista_autores.reverse()

        for i in range (len (self.api_lista_autores)):
            print("imprime por posicion")
            print(self.api_lista_autores)
            
            for j in range (len (self.api_lista_autores[i])):
                print("imprime por posicion de las hijas")
                print(self.api_lista_autores[i][j])
