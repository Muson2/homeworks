import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QHBoxLayout, QLineEdit, QLabel, QMessageBox, QTextEdit, QInputDialog
)
from PyQt6.QtGui import QRegExpValidator
from PyQt6.QtCore import QRegExp

import crud_alt

class UserApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User CRUD (PyQt6)")
        self.setGeometry(100, 100, 600, 500)

        crud_alt.create_table()

        self.layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.birth_input = QLineEdit()

        
        date_validator = QRegExpValidator(QRegExp(r"\d{4}-\d{2}-\d{2}"))
        self.birth_input.setValidator(date_validator)

        self.layout.addWidget(QLabel("Имя:"))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(QLabel("Возраст:"))
        self.layout.addWidget(self.age_input)
        self.layout.addWidget(QLabel("Email:"))
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(QLabel("Телефон:"))
        self.layout.addWidget(self.phone_input)
        self.layout.addWidget(QLabel("Дата рождения (ГГГГ-ММ-ДД):"))
        self.layout.addWidget(self.birth_input)

        btn_layout = QHBoxLayout()

        self.add_btn = QPushButton("Добавить")
        self.update_btn = QPushButton("Обновить по ID")
        self.list_btn = QPushButton("Показать всех")
        self.find_btn = QPushButton("Найти")
        self.delete_btn = QPushButton("Удалить по ID")

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.list_btn)
        btn_layout.addWidget(self.find_btn)
        btn_layout.addWidget(self.delete_btn)

        self.layout.addLayout(btn_layout)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.layout.addWidget(self.output)

        self.setLayout(self.layout)

        self.add_btn.clicked.connect(self.add_user)
        self.update_btn.clicked.connect(self.update_user)
        self.list_btn.clicked.connect(self.show_users)
        self.find_btn.clicked.connect(self.find_user)
        self.delete_btn.clicked.connect(self.delete_user)

    def is_valid_date(self, date_text):
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def add_user(self):
        name = self.name_input.text()
        age = self.age_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        birth_date = self.birth_input.text().strip() or None

        if not name or not age:
            QMessageBox.warning(self, "Ошибка", "Имя и возраст обязательны.")
            return

        try:
            age = int(age)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Возраст должен быть числом.")
            return

        if birth_date and not self.is_valid_date(birth_date):
            QMessageBox.warning(self, "Ошибка", "Неверный формат даты (ГГГГ-ММ-ДД).")
            return

        try:
            crud_alt.insert_user(name, age, email, phone, birth_date)
            self.output.append(f"[+] Добавлен: {name}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка при добавлении", str(e))

    def update_user(self):
        user_id, ok = QInputDialog.getInt(self, "Обновить", "Введите ID пользователя:")
        if ok:
            name = self.name_input.text()
            age = self.age_input.text()
            email = self.email_input.text()
            phone = self.phone_input.text()
            birth_date = self.birth_input.text().strip() or None

            if not name or not age:
                QMessageBox.warning(self, "Ошибка", "Имя и возраст обязательны.")
                return

            try:
                age = int(age)
            except ValueError:
                QMessageBox.warning(self, "Ошибка", "Возраст должен быть числом.")
                return

            if birth_date and not self.is_valid_date(birth_date):
                QMessageBox.warning(self, "Ошибка", "Неверный формат даты (ГГГГ-ММ-ДД).")
                return

            try:
                count = crud_alt.update_user(user_id, name, age, email, phone, birth_date)
                if count:
                    self.output.append(f"[Обновление] Пользователь ID={user_id} обновлён")
                else:
                    self.output.append("[!] Пользователь не найден.")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка обновления", str(e))

    def show_users(self):
        conn = crud_alt.connect_db()
        users = conn.execute("SELECT * FROM users").fetchall()
        self.output.clear()
        for u in users:
            self.output.append(f"{u[0]} | {u[1]} | {u[2]} | {u[3]} | {u[4]} | {u[5] or '-'}")
        conn.close()

    def find_user(self):
        keyword, ok = QInputDialog.getText(self, "Поиск", "Введите имя/email/телефон:")
        if ok and keyword:
            conn = crud_alt.connect_db()
            sql = "SELECT * FROM users WHERE name LIKE ? OR email LIKE ? OR phone LIKE ?"
            results = conn.execute(sql, [f"%{keyword}%"] * 3).fetchall()
            conn.close()
            self.output.clear()
            if results:
                for u in results:
                    self.output.append(f"{u[0]} | {u[1]} | {u[2]} | {u[3]} | {u[4]} | {u[5] or '-'}")
            else:
                self.output.append("[!] Ничего не найдено.")

    def delete_user(self):
        user_id, ok = QInputDialog.getInt(self, "Удаление", "Введите ID пользователя:")
        if ok:
            confirm = QMessageBox.question(
                self, "Подтвердите", f"Удалить пользователя с ID={user_id}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if confirm == QMessageBox.StandardButton.Yes:
                conn = crud_alt.connect_db()
                cur = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
                conn.commit()
                if cur.rowcount:
                    self.output.append(f"[−] Удалён пользователь ID={user_id}")
                else:
                    self.output.append("[!] Пользователь не найден.")
                conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UserApp()
    win.show()
    sys.exit(app.exec())
