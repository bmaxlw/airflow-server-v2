import psycopg2

class DatabaseManager:

    def __init__(self, hostname: str, port: str, username: str, password: str, database: str) -> None:
        self.connection = psycopg2.connect(database=database, user=username, password=password, host=hostname,port=port)

    def run_sql_script(self, sql_path: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(open(sql_path, "r").read())
        self.connection.commit()
        self.connection.close()
