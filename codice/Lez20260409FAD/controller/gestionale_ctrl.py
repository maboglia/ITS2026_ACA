from model.employee import Employee
from model.customer import Customer
from repos.employee_dao import EmployeeDAO



class GestionaleController:
    def __init__(self, model):
        self.dao = EmployeeDAO()
        self.impiegati = self.dao.list_employees()

    def add_employee(self, name, surname, title):
        employee = Employee(name, surname, title)
        self.impiegati.append(employee)

    def list_employees(self):
        return self.impiegati
    
    def find_employee_by_id(self, employee_id):
        return self.dao.find_employee_by_id(employee_id)