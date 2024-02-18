import sys
from weather import main as go_weather
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QGridLayout, QMainWindow
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_settings()
        self.labels()
        self.buttons()
        self.layouts()
        self.load_images('zastavka.jpg')
        self.setLayout(self.layout)

    def window_settings(self):
        self.setGeometry(400, 100, 1250, 850)
        self.setWindowTitle("Узнаем погодку")

    def labels(self):
        self.label = QLabel("Хочешь узнать погодку?")
        self.label.setFont(QFont('Arial', 10))
        self.weather = QLabel(go_weather())

    def buttons(self):
        self.button = QPushButton("Хочу!")
        self.button.clicked.connect(self.button_clicked)

    def layouts(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.weather, alignment=Qt.AlignmentFlag.AlignCenter)

    def button_clicked(self):
        self.layout.addWidget(self.weather, alignment=Qt.AlignmentFlag.AlignCenter)

    def load_images(self, file_name):
        self.background = QPixmap(file_name)
        self.label_back = QLabel(self)
        self.label_back.setPixmap(self.background)
        self.label_back.resize(self.background.width(), self.background.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()