import sqlite3

DB_PATH = "users.db"

def connect_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            job TEXT
        )   
    """)
    conn.commit()
    conn.close()


def update_user(user_id, name=None, age=None, email=None, phone=None, job=None):
    conn = connect_db()
    cursor = conn.cursor()
    fields = []
    values = []

    if name:
        fields.append("name = ?")
        values.append(name)
    if age:
        fields.append("age = ?")
        values.append(age)
    if email:
        fields.append("email = ?")
        values.append(email)
    if phone:
        fields.append("phone = ?")
        values.append(phone)
    if job:
        fields.append("job = ?")
        values.append(job)

    if not fields:
        return 0

    values.append(user_id)
    cursor.execute(f"UPDATE users SET {', '.join(fields)} WHERE id = ?", values)
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated
