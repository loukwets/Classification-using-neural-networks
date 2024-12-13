# WETS Loukas mat.ULB: 000442311
"""
THIS FILE CONTAINS THE CLASS Neurones.
"""

from PyQt4 import QtGui, QtCore, QtTest
import numpy

class Neurones(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.W1= numpy.ones(784)
        self.W2= numpy.ones(10)

    def handle(self, W1, W2):
        """Methode qui met a jour le paintEvent avec le nouveau
            Dropout.
        """
        self.W1, self.W2 = W1, W2
        self.update()
        QtTest.QTest.qWait(1)

    def paintEvent(self, event):
        """Msthode qui dessine l'état des neuronnes celon
            le Dropout.
        """
        painter = QtGui.QPainter(self)
        for i in range(49):
            for j in range(16):
                center = QtCore.QPoint((j+12)*12, (i+1)*12)
                if self.W1[(i*16)+j] == 0:
                    painter.setPen(QtGui.QPen(QtCore.Qt.red))
                else :
                    painter.setPen(QtGui.QPen(QtCore.Qt.green))
                painter.drawEllipse(center, 5, 5)
    
        y = 441/(len(self.W2)+1)
        for z in range(len(self.W2)):
            center = QtCore.QPoint(600, (z+1)*y)
            if self.W2[z] == 0:
                painter.setPen(QtGui.QPen(QtCore.Qt.red))
            else :
                painter.setPen(QtGui.QPen(QtCore.Qt.green))
            painter.drawEllipse(center, 10, 10)
