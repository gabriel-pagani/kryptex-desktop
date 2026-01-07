import sqlite3


DB_FILE = 'db.sqlite3'


def get_connection():
    return sqlite3.connect(DB_FILE)


def execute_query(query: str, param = None):
    with get_connection() as conn:
        cursor = conn.cursor()

        if param is not None:
            cursor.execute(query, param)
        else:
            cursor.execute(query)

        if cursor.description is not None:
            return cursor.fetchall()
