class Figura:
    def area(self):
        pass
    def perimetro(self):
        pass

class FiguraSpigolosa:
    pass

class Rettangolo(Figura, FiguraSpigolosa):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)

class Quadrato(Rettangolo):
    def __init__(self, lato):
        super().__init__(lato, lato)

q1 = Quadrato(5)
r1 = Rettangolo(4, 6)

print(isinstance(r1, Quadrato))

print(q1.area())
print(q1.perimetro())
