import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber, QLineEdit, QMainWindow, QButtonGroup

from criss_cross import Ui_MainWindow


class MyProgram(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.field = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.btn00)
        self.btn_group.addButton(self.btn10)
        self.btn_group.addButton(self.btn20)
        self.btn_group.addButton(self.btn01)
        self.btn_group.addButton(self.btn11)
        self.btn_group.addButton(self.btn21)
        self.btn_group.addButton(self.btn02)
        self.btn_group.addButton(self.btn12)
        self.btn_group.addButton(self.btn22)

        for x in range(3):
            for y in range(3):
                self.btn_group.buttons()[(x + 1) * (y + 1) - 1].clicked.connect(lambda a, i=x, j=y: self.change_value(i, j))

    def change_value(self, x, y):
        print(x, y)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyProgram()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
