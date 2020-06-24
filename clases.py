class Persona:
    # Atributos
    # Métodos
    def __init__(self, nombre, edad):  # Método constructor
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        texto = "Persona: ("
        texto = texto + self.nombre + ":"
        texto = texto + str(self.edad) + ") "
        return texto


def verLista(datos):
    i = 1
    texto = "LISTA: \n"
    for personaX in datos:
        linea = "[{}]: {}\n".format(i, personaX)
        i = i + 1
        texto = texto + linea
    texto = texto + "......................Fin de la x_list.\n"
    return texto


class Lista:
    def __init__(self):
        self.lista = []

    def adicionar(self, obj):
        self.lista.append(obj)

    def __str__(self):
        return verLista(self.lista)

    def __len__(self):
        return len(self.lista)

    def cambiarLista(self, lista):
        self.lista = lista
