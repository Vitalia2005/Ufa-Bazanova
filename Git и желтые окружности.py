import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen


class CirclesMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circles = []
        self.draw_btn.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(1, min([self.width(), self.height()]))
        x = random.randint(0, self.width() - diameter - 1)
        y = random.randint(0, self.height() - diameter - 1)
        self.circles += [((255, 255, 0), (x, y, diameter, diameter))]
        self.update()

    def draw_circles(self, qp):
        qp.setBrush(QColor(0, 0, 0, 0))
        for color, data in self.circles:
            pen = QPen(QColor(*color), 5)
            qp.setPen(pen)
            qp.drawEllipse(*data)

    def paintEvent(self, *args, **kwargs):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CirclesMainWindow()
    window.show()
    sys.exit(app.exec())
