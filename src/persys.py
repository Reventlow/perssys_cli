import pyodbc
from decouple import config


class PersysDB:
    def __init__(self):
        self.connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={{config("DB_SERVER")}};'
            f'DATABASE={{config("DB_NAME")}};'
            f'UID={{config("DB_USER")}};'
            f'PWD={{config("DB_PASSWORD")}}'
        )
        self.cursor = self.connection.cursor()

    def find_user(self, username):
        query = """
        SELECT 
            [Brugernavn], [Fornavn], [Efternavn], [E-mail adresse], [Telefon, direkte],
            [Placering, Forkortelse], [Primær title], [Afdeling, Navn],
            [Startdato], [Slutdato], [Primær chef, Navn], [Primær chef, Brugernavn]
        FROM persys
        WHERE [Brugernavn] = ?
        """
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()

    def get_all_users_for_fuzzy(self):
        query = """
        SELECT 
            [Brugernavn], [Fornavn], [Efternavn], [Afdeling, Navn]
        FROM persys
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
