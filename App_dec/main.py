import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from ui_untitled import Ui_MainWindow

def resource_path(relative_path):
    """Возвращает правильный путь к ресурсу в скомпилированном .exe или для разработки."""
    try:
        # Для скомпилированного .exe
        base_path = sys._MEIPASS
    except Exception:
        # Для обычной разработки
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Загружаем изображения с правильным путем
        self.label_3.setPixmap(QPixmap(resource_path("img/331a046af78255a2d0642af437bc9d22.png")))
        self.label_5.setPixmap(QPixmap(resource_path("img/unnamed.png")))
        self.label_7.setPixmap(QPixmap(resource_path("img/588267.png")))
        self.label_9.setPixmap(QPixmap(resource_path("img/tumblr_pkpdu2ffr31tx3jbk_400.jpg")))

        # Пример обработчика для кнопки
        self.btn_go.clicked.connect(self.on_click_btn_go_cs2)
        self.btn_go.clicked.connect(self.on_click_btn_go_cs2)

    def on_click_btn_go_cs2(self):
        print('Click')
        # Ваши действия при нажатии кнопки
        steam_path = r"C:\ALL\PROGRAMS\steam.exe"
        discord = r'C:\Users\ar2rf\AppData\Local\Discord\Update.exe --processStart Discord.exe'
        app_id = 730
        os.system(f'"{steam_path}" -applaunch {app_id}')
        os.system(f'"{discord}"')


# Запуск приложения
app = QApplication(sys.argv)
window = MainWindow()  # Используем свой класс MainWindow
window.show()  # Показываем окно
sys.exit(app.exec())  # Запуск главного цикла приложения
