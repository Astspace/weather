import sys
from weather import main as go_weather
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize, Qt


class MainWindow(QWidget):
    button_clicked_count = 0
    def __init__(self):
        super().__init__()
        self._load_image_background('zastavka.jpg')
        self._buttons()
        self._labels()
        self._window_settings()

    def _window_settings(self) -> None:
        self.setGeometry(400, 100, 1250, 850)
        self.setWindowTitle("Узнаем погодку")

    def _labels(self) -> None:
        self.label = QLabel("Хочешь узнать погодку?", self)
        self.label.setFont(QFont('Arial', 30))
        self.label.move(10, 500)

    def _buttons(self) -> None:
        self.button = QPushButton("Мяу!", self)
        self.button.move(100, 200)
        self.button.clicked.connect(self._button_clicked)

    def _button_clicked(self) -> None:
        if self.button_clicked_count == 0:
            self.label_weather = QLabel(go_weather(), self)
            self.label_weather.setFont(QFont('Arial', 10))
            self.label_weather.move(10, 500)
            self.label_weather.show()
            self.button.setText("Обновить данные")
            self.button_clicked_count += 1
            self._load_images("4.png")

        else:
            self.label_weather.deleteLater()
            self.label_weather = QLabel(go_weather(), self)
            self.label_weather.setFont(QFont('Arial', 10))
            self.label_weather.move(10, 500)
            self.label_weather.show()
            self.button.setText("Обновить данные")
            self._load_images("4.png")

    def _load_image_background(self, file_name: str) -> None:
        image = QPixmap(file_name)
        label_image = QLabel(self)
        label_image.setPixmap(image)
        label_image.resize(image.width(), image.height())
        print(image.width(), image.height())

    def _load_images(self, file_name: str):
        image1 = (QPixmap(file_name).scaled(600, 400, Qt.AspectRatioMode.KeepAspectRatio))
        label_image1 = QLabel(self)
        label_image1.setPixmap(image1)
        label_image1.show()
        label_image1.move(0, 0)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()