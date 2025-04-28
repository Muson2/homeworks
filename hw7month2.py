import sqlite3

class Task:
    def __init__(self, dbname = "todo.db"):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                is_done BOOLEAN      
            )
        """)
        self.conn.commit()

    def save(self, title, description, is_done):
        self.cursor.execute("INSERT INTO tasks (title, description, is_done) VALUES (?, ?, ?)", (title, description, is_done))
        self.conn.commit()
        self.is_done = is_done

    def delete(self, title):
        self.cursor.execute("DELETE FROM tasks WHERE title = ?", (title,))
        self.conn.commit()

    def mark_done(self, title, is_done):
        self.cursor.execute("UPDATE tasks SET is_done = ? WHERE title = ?", (is_done, title))

    def get_all_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()

    def get_pending_tasks(self):
        self.cursor.execute("SELECT * FROM tasks WHERE is_done = 0")
        return self.cursor.fetchall()

    def get_task_by_id(self, task_id):
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        return self.cursor.fetchone()

    def close(self):
      self.conn.close()

task = Task()
task.save("Пробежка", "Пробежка 10 км", False)
task.mark_done("Пробежка", True)
task.get_all_tasks()
task.get_pending_tasks()
task.get_task_by_id(1)
task.delete("Пробежка")
task.close()