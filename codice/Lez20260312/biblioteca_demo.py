from biblioteca import Biblioteca
from libro import Libro

biblioteca_civica = Biblioteca()

for libro in biblioteca_civica.getLibri():
    print(f"{libro}")
