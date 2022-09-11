import pymysql
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWD

connection = pymysql.connect (
    host = DB_HOST,
    port = DB_PORT,
    user = DB_USER,
    password = DB_PASSWD,
    database = DB_NAME,
    cursorclass = pymysql.cursors.DictCursor
)