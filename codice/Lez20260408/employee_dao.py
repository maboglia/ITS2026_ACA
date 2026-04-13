import database
from dataclasses import dataclass

@dataclass
class Impiegato:
    nome: str
    cognome: str
    ruolo: str
    



class EmployeeDao:

    def findImpiegati(self):
        DB_impiegati = database.connetti()
        impiegati = database.interroga(DB_impiegati, "select FirstName, LastName, Title from Employee")

        return [Impiegato(n,c,r)  for n, c, r in impiegati]
