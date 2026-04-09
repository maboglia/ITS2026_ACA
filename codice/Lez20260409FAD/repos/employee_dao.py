import mysql.connector
from model.employee import Employee

class EmployeeDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="Chinook"
        )

    def add_employee(self, employee: Employee):
        cursor = self.connection.cursor()
        query = "INSERT INTO employees (name, surname, title) VALUES (%s, %s, %s)"
        values = (employee.name, employee.surname, employee.title)
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    def list_employees(self):
        cursor = self.connection.cursor()
        query = "SELECT FirstName, LastName, Title FROM Employee"
        cursor.execute(query)
        results = cursor.fetchall()
        employees = [Employee(name=row[0], surname=row[1], title=row[2]) for row in results]
        cursor.close()
        return employees

    def find_employee_by_id(self, employee_id):
        cursor = self.connection.cursor()
        query = "SELECT FirstName, LastName, Title FROM Employee WHERE EmployeeId = %s"
        cursor.execute(query, (employee_id,))
        result = cursor.fetchone()
        if result:
            employee = Employee(name=result[0], surname=result[1], title=result[2])
            cursor.close()
            return employee
        cursor.close()
        return None