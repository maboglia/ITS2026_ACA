from employee_dao import Impiegato, EmployeeDao
import json
dao = EmployeeDao()

print(json.dumps([i.__dict__ for i in dao.findImpiegati()]))


