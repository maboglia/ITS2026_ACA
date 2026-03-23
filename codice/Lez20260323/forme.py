
class Shape:
    def __init__(self, color): 
        self.color = color

    def __str__(self):
        return f"Sono una forma di colore {self.color}"    

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def __str__(self):
        descrizione = super().__str__()
        descrizione += f"\nSono un CERCHIO di superficie {3.14 * self.radius * self.radius}"
        return descrizione      

class Triangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

class Square(Shape):
    def __init__(self, width, color):
        super().__init__(color)
        self.width = width


cerchio = Circle(5, 'red')
triangolo = Triangle(4, 6, 'green')
quadrato = Square(7, 'blue')

print(type(cerchio))
print(triangolo)
print(quadrato)
