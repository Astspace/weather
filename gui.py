import sys
from weather import main as go_weather
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.load_images('zastavka.jpg')
        self.buttons()
        self.labels()
        self.window_settings()

    def window_settings(self):
        self.setGeometry(400, 100, 1250, 850)
        self.setWindowTitle("Узнаем погодку")

    def labels(self):
        self.label = QLabel("Хочешь узнать погодку?", self)
        self.label.setFont(QFont('Arial', 30))
        self.label.move(10, 500)

    def buttons(self):
        self.button = QPushButton("Хочу!", self)
        self.button.move(100, 200)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.label_weather = QLabel(go_weather(), self)
        self.label_weather.setFont(QFont('Arial', 10))
        self.label_weather.move(10, 500)
        self.label_weather.show()

    def load_images(self, file_name):
        self.image = QPixmap(file_name)
        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.image)
        self.label_image.resize(self.image.width(), self.image.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()