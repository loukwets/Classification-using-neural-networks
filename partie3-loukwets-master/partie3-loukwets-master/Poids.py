# WETS Loukas mat.ULB: 000442311
"""
THIS FILE CONTAINS THE CLASS Tableaux.
"""
from PyQt4 import QtGui, QtCore, QtTest
import numpy

class Tableaux(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        W = numpy.zeros((10,784))
        self.initUI(W)

    def updateTableau(self, W):
        """Methode qui introduit les valeurs dans les tableaux.
        """
        if len(W) == 10:
            #if H == 10.
            for n in range(10):
                for i in range(28):
                    for j in range(28):
                        newitem = QtGui.QTableWidgetItem(str(W[n][(i*28)+j]))
                        self.tables[n].setItem(i, j, newitem)
                self.tables[n].resizeColumnsToContents()
                self.tables[n].resizeRowsToContents()

    def initUI(self, W):
        """Methode qui crée les dix tableaux pour affiche
            les poids.
        """
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        self.tables = [QtGui.QTableWidget(self) for i in range(10)]
        for n in range(10):
            self.tables[n].setRowCount(28)
            self.tables[n].setColumnCount(28)
            grid.addWidget(self.tables[n], n//2, n%2)
        self.updateTableau(W)
