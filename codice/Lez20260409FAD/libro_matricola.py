from controller.gestionale_ctrl import GestionaleController


ctrl = GestionaleController(None)

impiegati = ctrl.list_employees()

# for imp in impiegati:
#     print(imp)

print(ctrl.find_employee_by_id(1))