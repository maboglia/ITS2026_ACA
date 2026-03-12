from libro import Libro
from libro_dao import tabella_libri

class Biblioteca:

    libreria= []

    def __init__(self):
        self.libreria = tabella_libri

    def addLibro(self, libro: Libro):
        self.libreria.append(libro)

    def getLibri(self):
        return self.libreria