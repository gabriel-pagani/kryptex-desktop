import sqlite3


DB_FILE = 'db.sqlite3'


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def execute_query(query: str, param = None):
    with get_connection() as conn:
        cursor = conn.cursor()

        if param is not None:
            cursor.execute(query, param)
        else:
            cursor.execute(query)

        if cursor.description is not None:
            return cursor.fetchall()
