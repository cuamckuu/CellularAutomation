from main import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

EDGE = 5
HEIGHT = 600

class View(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.field = ["0"]*250
        self.field[125] = "1"
        self.fields = [self.field]

        #Update painter animation
        updater = QTimer(self)
        updater.start(50)
        updater.timeout.connect(self.update)

        self.img = QPixmap(EDGE*len(self.field), HEIGHT)
        self.img.fill(QColor(255, 255, 255))

        #Window size
        self.setMinimumSize(QSize(EDGE*len(self.field), HEIGHT))
        self.setMaximumSize(QSize(EDGE*len(self.field), HEIGHT))
        self.setWindowTitle('Patterns')
        self.show()

    def paintEvent(self, e):
        """Paint board due to self.game.board"""

        #Draw board 
        qp = QPainter()
        qp.begin(self.img)
        for i, field in enumerate(self.fields):
            for j, ch in enumerate(field):
                if ch == "1":
                    qp.setBrush(QColor(0, 0, 0))
                else:
                    qp.setBrush(QColor(255, 255, 255))
                qp.drawRect(j*EDGE, i*EDGE, EDGE, EDGE)
        qp.end()

        qp.begin(self)
        qp.drawPixmap(QPoint(0,0), self.img)
        qp.end()

        del qp

        self.field = generate(self.field)
        self.fields += [self.field]

        if len(self.fields)*EDGE >= HEIGHT:
            self.fields = self.fields[1:]
        
        

app = QApplication([])
view = View()
app.exec()