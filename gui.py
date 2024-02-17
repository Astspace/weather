import sys
from weather import main as go_weather
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_settings()
        self.labels()
        self.buttons()
        self.layouts()
        self.setLayout(self.layout)

    def window_settings(self):
        self.setGeometry(700, 300, 350, 250)
        self.setWindowTitle("Узнаем погодку")

    def labels(self):
        self.label = QLabel("Погодка:")
        self.label.setFont(QFont('Arial', 10))
        self.weather = QLabel(go_weather())

    def buttons(self):
        self.button = QPushButton("GO")

    def layouts(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.weather, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()