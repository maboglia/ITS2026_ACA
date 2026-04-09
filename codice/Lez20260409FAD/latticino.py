class Prodotto:
    def __init__(self):
        print("Nuovo prodotto")


class Latticino(Prodotto):
    def __init__(self, nome, peso):
        super().__init__()
        self.nome = nome
        self.peso = peso

    def __str__(self):
        return f"{self.nome} ({self.peso} kg)"
    

class Mozzarella(Latticino):
    def __init__(self, nome, peso, tipo):
        super().__init__(nome, peso)
        self.tipo = tipo


cacio = Latticino("cacio", 1)

m1 = Mozzarella("Ciliegino", 0.2, "Bufalino")
print(m1)
print(cacio)

