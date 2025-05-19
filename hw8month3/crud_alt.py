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
            age INTEGER,
            email TEXT UNIQUE,
            phone TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def sanitize(value):
    return value if value and value.strip() else None

def insert_user(name, age, email, phone, status):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (name, age, email, phone, status)
            VALUES (?, ?, ?, ?, ?)
        """, (name, age, sanitize(email), sanitize(phone), sanitize(status)))
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise Exception(f"Ошибка добавления: {e}")
    finally:
        conn.close()

def update_user(user_id, name, age, email, phone, status):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE users
            SET name = ?, age = ?, email = ?, phone = ?, status = ?
            WHERE id = ?
        """, (name, age, sanitize(email), sanitize(phone), sanitize(status), user_id))
        conn.commit()
        return cursor.rowcount
    except sqlite3.IntegrityError as e:
        raise Exception(f"Ошибка обновления: {e}")
    finally:
        conn.close()
