import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                    )"""
        self.conn.execute(query)
        self.conn.commit()

    def validate_user(self, username, password):
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (username, password))
        return cursor.fetchone() is not None

    def add_user(self, username, password):
        try:
            query = "INSERT INTO users (username, password) VALUES (?, ?)"
            self.conn.execute(query, (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
