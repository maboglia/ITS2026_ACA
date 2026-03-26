# driver mysql: pip install mysql-connector-python

import mysql.connector

class Connessione:

    def __init__(self):
        pass

    def connetti(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'magazzino'
        )
        if self.db:
            print('sei connesso al db')
            return self.db
        else:
            print('non connesso al db')


    def chiudi(self):
        if self.db.is_connected():
            self.db.close()

if __name__ == '__main__':
    conn = Connessione()
    conn.connetti()
    conn.chiudi()