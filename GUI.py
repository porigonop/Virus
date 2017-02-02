from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRect, QLine, QPoint
from VirusGame import VirusGame



class GUI(QWidget):
    name_to_color = {"." : QColor(0, 0, 0),
                     "x" : QColor(255, 0, 0),
                     "o" : QColor(0, 255, 255),
                     "+" : QColor(0, 0, 255),
                     "*" : QColor(125, 125, 125)
                     }
    def __init__(self):
        super().__init__()
        self.game = VirusGame(3)
        self.initUI()
    
    def initUI(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Virus Game")
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawgame(qp)
        qp.end()

    def drawgame(self, qp):
        for index_x in range(len(self.game.grid.grid)):
            for index_y in range(len(self.game.grid.grid[index_x])):
                qp.setBrush(GUI.name_to_color[self.game.grid.grid[index_x][index_y].color])

