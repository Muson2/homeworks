import sqlite3

class DBHelper:
    def __init__(self, dbname="users.db"):
        self.conn = sqlite3.connect(dbname)
        self.conn.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE,
            city TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()

    def add_user(self, name, age, email, city):
        self.conn.execute("""
        INSERT INTO users (name, age, email, city)
        VALUES (?, ?, ?, ?)
        """, (name, age, email, city))
        self.conn.commit()

    def get_users_by_age_range(self, min_age, max_age):
        cursor = self.conn.execute("""
        SELECT * FROM users WHERE age BETWEEN ? AND ?
        """, (min_age, max_age))
        return cursor.fetchall()

    def get_recent_users(self, n):
        cursor = self.conn.execute("""
        SELECT * FROM users ORDER BY created_at DESC LIMIT ?
        """, (n,))
        return cursor.fetchall()

db = DBHelper()
db.add_user("Усон", 28, "elena@example.com", "Москва")
db.add_user("Асан", 35, "igor@example.com", "Казань")
db.add_user("Аслан", 22, "nata@example.com", "Москва")

print("Пользователи 25–35 лет:")
for user in db.get_users_by_age_range(25, 35):
    print(dict(user))

print("\nПоследние 2 добавленных пользователя:")
for user in db.get_recent_users(2):
    print(dict(user))
