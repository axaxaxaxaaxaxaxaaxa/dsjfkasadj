import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
from random import randint


class VeryComplicatedInterface:
    def __init__(self, window):
        self.window = window
        self.window.setGeometry(0, 0, 800, 600)
        self.window.setWindowTitle("Вставить текст")
        self.button = QPushButton(window)
        self.button.setGeometry(270, 540, 271, 51)
        self.button.setText("Жми яростнее")


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.interface = VeryComplicatedInterface(self)
        self.draw = False
        self.interface.button.clicked.connect(self.activate)

    def activate(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        self.draw = True
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        size = randint(20, 200)
        qp.drawEllipse(randint(0, 600), randint(0, 400), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())