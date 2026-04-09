class Employee:
    def __init__(self, name, surname, title):
        self.name = name
        self.surname = surname
        self.title = title

    def __str__(self):
        return f"{self.name} {self.surname} - Title: {self.title}"