import sys
from weather import main as go_weather
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from PyQt6.QtGui import QPixmap, QColor, QIcon
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    button_clicked_count = 0
    def __init__(self):
        super().__init__()
        self._load_image_background('zastavka.jpg')
        self._load_images("4.png", 470, 470, -10, 180)
        self._buttons()
        self._labels()
        self._window_settings()

    def _window_settings(self) -> None:
        self.setGeometry(400, 100, 1250, 850)
        self.setWindowTitle("Узнаем погодку")

    def _labels(self) -> None:
        self.label = QLabel("Хочешь узнать погодку?", self)
        self.label.setStyleSheet(f'color: {QColor(255, 228, 225).name()}')
        self.label.setFont(QFont('Cambria', 15))
        self.label.move(120, 230)

    def _buttons(self) -> None:
        self.button = QPushButton("МЯУ!", self)
        self.button.setStyleSheet('QPushButton {font-size: 16px;'
                                  'background-color: #e9c8e9;'
                                  'color: #6572c2;'
                                  'font-weight: bold}')
        self.button.setGeometry(160, 270, 130, 35)
        self.button.setIcon(QIcon('cat.png'))
        self.button.clicked.connect(self._button_clicked)

    def _button_clicked(self) -> None:
        if self.button_clicked_count == 0:
            self._load_images("3.png", 450, 350, 830, 10)
            self._load_images("1.png", 400, 300, 25, -65)
            self._get_data_weather()
        else:
            self.label_weather.deleteLater()
            self._get_data_weather()

    def _load_image_background(self, file_name: str) -> None:
        image = QPixmap(file_name)
        image_background = QLabel(self)
        image_background.setPixmap(image)
        image_background.resize(image.width(), image.height())

    def _load_images(
            self,
            file_name: str,
            width: int,
            height: int,
            ax: int,
            ay: int) -> None:
        image = (QPixmap(file_name)
                 .scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio))
        loaded_image = QLabel(self)
        loaded_image.setPixmap(image)
        loaded_image.show()
        loaded_image.move(ax, ay)

    def _get_data_weather(self) -> None:
        self.label_weather = QLabel(go_weather(), self)
        self.label_weather.setFont(QFont('Cambria', 13))
        self.label_weather.setStyleSheet(f'color:{QColor(255, 235, 225).name()}')
        self.label_weather.move(70, 240)
        self.label_weather.show()
        self.button.setText("Обновить данные")
        self.button.move(70, 400)
        self.button.setStyleSheet('QPushButton {font-size: 14px;'
                                  'background-color: #e9c8e9;'
                                  'color: #963b6c}')
        self.button.setIcon(QIcon(''))
        self.label.setText("")
        self.button_clicked_count += 1


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()