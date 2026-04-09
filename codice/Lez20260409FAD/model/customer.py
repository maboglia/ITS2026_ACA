from model.employee import Employee

class Customer:
    def __init__(self, name: str, surname: str, email: str, employee: Employee):
        self.name = name
        self.surname = surname
        self.email = email
        self.employee = employee

    def __str__(self):
        return f"{self.name} {self.surname} - Email: {self.email}"