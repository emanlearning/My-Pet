import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor


class DesktopPet(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Desktop Pet")
        self.resize(300, 300)

        # make the window borderless, always stay on top of other app and transparent.
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHints(QPainter.RenderHint.Antialiasing)

        # flame body
        painter.setPen(Qt.PenStyle.NoPen)

        # flame
        flame_color = QColor(120, 195, 252, 230)
        painter.setBrush(QBrush(flame_color))

        # flame drawing and placement
        painter.drawEllipse(95, 50, 90, 90)

        # eye
        eye_color = QColor(15, 45, 90)
        painter.setBrush(QBrush(eye_color))

        # eyes placement
        painter.drawEllipse(115, 80, 14, 15)
        painter.drawEllipse(150, 80, 14, 15)

        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    pet = DesktopPet()

    pet.show()

    sys.exit(app.exec())
