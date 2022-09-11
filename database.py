import pymysql

class _Database_:

    def __init__(self, DB_HOST: str, DB_PORT: int, DB_NAME: str, DB_USER: str, DB_PASSWD: str) -> None:
        
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_NAME = DB_NAME
        self.DB_USER = DB_USER
        self.DB_PASSWD = DB_PASSWD

        self.connection = pymysql.connect (
            host = DB_HOST,
            port = DB_PORT,
            user = DB_USER,
            password = DB_PASSWD,
            database = DB_NAME,
            cursorclass = pymysql.cursors.DictCursor
        )
        
    def select(self, sql: str) -> dict:

        with self.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(sql)
            return cursor.fetchone()
