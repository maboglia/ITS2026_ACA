
class Film:

    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating

    def __str__(self):
        return f"Il film '{self.title}' è del {self.year}"