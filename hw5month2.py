import sqlite3

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    product TEXT,
    quantity INTEGER
)
''')


cursor.execute("INSERT INTO orders (name, product, quantity) VALUES (?, ?, ?)", ("Алиса", "Ноутбук", 1))
cursor.execute("INSERT INTO orders (name, product, quantity) VALUES (?, ?, ?)", ("Боб", "Монитор", 2))
cursor.execute("INSERT INTO orders (name, product, quantity) VALUES (?, ?, ?)", ("Чарли", "Клавиатура", 3))

conn.commit()