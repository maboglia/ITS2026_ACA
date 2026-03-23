class Animal:
    def __init__(self, nome):
        self.nome = nome

class Predatore(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def caccia(self):
        print(f"{self.nome} sta cacciando")

class Preda(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def scappa(self):
        print(f"{self.nome} sta scappando")

class Tigre(Predatore):
    def __init__(self, nome):
        super().__init__(nome)
        print("Oggetto di tipo tigre costuito")

class Gazzella(Preda):
    def __init__(self, nome):
        super().__init__(nome)
        print("Oggetto di tipo gazzella costuito")

class Pesce(Predatore, Preda):
    def __init__(self, nome):
        super().__init__(nome)
        print("Oggetto di tipo pesce costuito")

hobbes = Tigre("tigre")
gazza = Gazzella("gazzella")
nemo = Pesce("pesce rosso")

hobbes.caccia()
gazza.scappa()
nemo.scappa()
nemo.caccia()