import pytds
from decouple import config


class PerssysDB:
    def __init__(self):
        self.connection = pytds.connect(
            server=config("DB_SERVER"),
            port=int(config("DB_PORT")),
            database=config("DB_NAME"),
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            timeout=10
        )
        self.cursor = self.connection.cursor()

    def find_user(self, username):
        query = """
        SELECT 
            [Brugernavn], [Fornavn], [Efternavn], [E-mail adresse], [Telefon, direkte],
            [Placering, Forkortelse], [Primær titel], [Afdeling, Navn],
            [Startdato], [Slutdato], [Primær chef, Navn], [Primær chef, Brugernavn]
        FROM Unord_View
        WHERE [Brugernavn] = %s
        """
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()

    def get_all_users_for_fuzzy(self):
        query = """
        SELECT 
            [Brugernavn], [Fornavn], [Efternavn], [Afdeling, Navn]
        FROM Unord_View
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()


if __name__ == "__main__":
    try:
        db = PerssysDB()
        print("\u2705 Connection successful.")
    except Exception as e:
        print("\u274C Connection failed:", e)
