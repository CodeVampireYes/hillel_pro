from PyQt6.QtWidgets import QApplication, QWidget



if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('First app')
    window.setGeometry(100, 100, 400, 300)
    window.show()
    app.exec()