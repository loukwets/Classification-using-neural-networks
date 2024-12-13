# WETS Loukas mat.ULB: 000442311
"""
THIS FILE CONTAINS THE CLASS Tableaux.
"""
from PyQt4 import QtGui, QtCore, QtTest
import numpy

class Tableaux(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        W = numpy.ones((10,784))
        self.initUI(W)

    def updatePixels(self, W):
        """Methode qui determine les pixels des images.
        """
        if len(W) == 10:
            #if H == 10.
            for n in range(10):
                minW = abs(numpy.amin(W[n]))
                maxW = 255/(numpy.amax(W[n])+minW)
                for x in range(28):
                    for y in range(28):
                        d = (W[n][(y*28)+x]+minW)*maxW          #Transphormer en nuance de gris.
                        self.imgs[n].setPixel(x, y, QtGui.QColor(d, d, d).rgb())
                self.pix = QtGui.QPixmap.fromImage(self.imgs[n])
                self.labels[n].setPixmap(self.pix.scaled(70, 70))

    def initUI(self, W):
        """Methode qui crée les dix tableaux pour affiche
            les poids.
        """
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        #self.tables = [QtGui.QTableWidget(self) for i in range(10)]
        self.labels = [QtGui.QLabel() for i in range(10)]
        self.imgs = [QtGui.QImage(28, 28, QtGui.QImage.Format_RGB888) for i in range(10)]
        for n in range(10):
            grid.addWidget(self.labels[n], n//2, n%2)
        self.updatePixels(W)
