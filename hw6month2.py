import sqlite3

class Library:
    def __init__(self, db_name="library.db"):

        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT
            )
        """)
        self.conn.commit()

    def add_book(self, title, author):
        
        self.cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        self.conn.commit()
        print(f"Книга '{title}' автора '{author}' успешно добавлена.")

    def delete_book(self, book_id):
        
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f"Книга с ID {book_id} успешно удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def list_books(self):
        
        self.cursor.execute("SELECT id, title, author FROM books")
        books = self.cursor.fetchall()
        if books:
            print("\nСписок всех книг:")
            for book in books:
                print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}")
        else:
            print("В библиотеке пока нет книг.")

    def close_connection(self):
        
        self.conn.close()


library = Library()
library.add_book("Мастер и Маргарита", "Михаил Булгаков")
library.add_book("1984", "Джордж Оруэлл")
library.add_book("Гордость и предубеждение", "Джейн Остин")
library.list_books()
library.delete_book(2)
library.list_books()
library.delete_book(5) 
library.close_connection()