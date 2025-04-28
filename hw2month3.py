import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import QTimer, Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

         
        self.label = QLabel("Текст до таймера", self)
        self.label.setStyleSheet("font-size: 24px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


        QTimer.singleShot(2000, self.update_label)

 
        self.setWindowTitle("QTimer и QLabel (PyQt6)")
        self.resize(400, 150)

    def update_label(self):
        self.label.setText("Текст после таймера!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
