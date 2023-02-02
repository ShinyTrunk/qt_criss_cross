import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber, QLineEdit, QMainWindow

from criss_cross import Ui_MainWindow


class MyProgram(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyProgram()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

