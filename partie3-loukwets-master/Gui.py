# WETS Loukas mat.ULB: 000442311
"""
THIS FILE CONTAINS THE CLASS Ui_MainWindow.
"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projet_d_annee.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
from Neurones import *
from Poids import *
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 650)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        #Choix du chiffre
        self.ChoixDuChiffre = QtGui.QComboBox(self.centralwidget)
        self.ChoixDuChiffre.setGeometry(QtCore.QRect(0, 30, 101, 26))
        self.ChoixDuChiffre.setObjectName(_fromUtf8("ChoixDuChiffre"))
        self.ChoixDuChiffre.addItem(_fromUtf8(""))
        self.ChoixDuChiffre.addItem(_fromUtf8(""))
        self.ChoixDuChiffre.addItem(_fromUtf8(""))
        self.ChoixDuChiffre.addItem(_fromUtf8(""))
        self.ChoixDuChiffre.addItem(_fromUtf8(""))
        self.ChoixDuChiffre.addItem(_fromUtf8(""))
        self.ChoixDuChiffre.addItem(_fromUtf8(""))
        self.ChoixDuChiffre.addItem(_fromUtf8(""))
        self.ChoixDuChiffre.addItem(_fromUtf8(""))
        self.ChoixDuChiffre.addItem(_fromUtf8(""))
        
        #Choix dataset
        self.choixDuDataset = QtGui.QComboBox(self.centralwidget)
        self.choixDuDataset.setGeometry(QtCore.QRect(100, 30, 121, 26))
        self.choixDuDataset.setObjectName(_fromUtf8("choixDuDataset"))
        self.choixDuDataset.addItem(_fromUtf8(""))
        self.choixDuDataset.addItem(_fromUtf8(""))
        self.choixDuDataset.addItem(_fromUtf8(""))
        
        #Alpha
        self.alpha = QtGui.QDoubleSpinBox(self.centralwidget)
        self.alpha.setGeometry(QtCore.QRect(220, 30, 68, 24))
        self.alpha.setSingleStep(0.01)
        self.alpha.setProperty("value", 0.5)
        self.alpha.setObjectName(_fromUtf8("alpha"))
        
        #Dropout
        self.PropDropout = QtGui.QDoubleSpinBox(self.centralwidget)
        self.PropDropout.setGeometry(QtCore.QRect(297, 30, 91, 24))
        self.PropDropout.setSingleStep(0.01)
        self.PropDropout.setProperty("value", 0.5)
        self.PropDropout.setObjectName(_fromUtf8("PropDropout"))
        
        #Epsilon
        self.Epsilon = QtGui.QDoubleSpinBox(self.centralwidget)
        self.Epsilon.setGeometry(QtCore.QRect(400, 30, 68, 24))
        self.Epsilon.setDecimals(4)
        self.Epsilon.setSingleStep(0.0001)
        self.Epsilon.setProperty("value", 0.0001)
        self.Epsilon.setObjectName(_fromUtf8("Epsilon"))
        
        #LearningRate
        self.LearningRate = QtGui.QDoubleSpinBox(self.centralwidget)
        self.LearningRate.setGeometry(QtCore.QRect(480, 30, 81, 24))
        self.LearningRate.setDecimals(3)
        self.LearningRate.setSingleStep(0.001)
        self.LearningRate.setProperty("value", 0.001)
        self.LearningRate.setObjectName(_fromUtf8("LearningRate"))
        
        #H
        self.H = QtGui.QSpinBox(self.centralwidget)
        self.H.setGeometry(QtCore.QRect(570, 30, 48, 24))
        self.H.setMinimum(1)
        self.H.setMaximum(20)
        self.H.setProperty("value", 10)
        self.H.setObjectName(_fromUtf8("H"))
        
        #Crossvalidation
        self.Crossvalidation = QtGui.QSpinBox(self.centralwidget)
        self.Crossvalidation.setGeometry(QtCore.QRect(630, 30, 101, 24))
        self.Crossvalidation.setMinimum(1)
        self.Crossvalidation.setProperty("value", 4)
        self.Crossvalidation.setObjectName(_fromUtf8("Crossvalidation"))
        
        #Training
        self.Training = QtGui.QSpinBox(self.centralwidget)
        self.Training.setGeometry(QtCore.QRect(740, 30, 71, 24))
        self.Training.setMinimum(1)
        self.Training.setProperty("value", 20)
        self.Training.setObjectName(_fromUtf8("Training"))
        
        #Bouton start
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(820, 30, 113, 32))
        self.start.setObjectName(_fromUtf8("start"))

        #Labels
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 41, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 10, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 10, 51, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 10, 81, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(590, 10, 16, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 10, 101, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(750, 10, 51, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        
        #Tabs
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(9, 79, 921, 500))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        #tab neurones
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        layout = QtGui.QGridLayout(self.tab)
        self.paint=Neurones()
        layout.addWidget(self.paint)
        
        #tab poids
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        layout2 = QtGui.QGridLayout(self.tab_2)
        self.poids=Tableaux()
        layout2.addWidget(self.poids)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Classification à l’aide de réseaux de neurones", None))
        self.ChoixDuChiffre.setItemText(0, _translate("MainWindow", "0", None))
        self.ChoixDuChiffre.setItemText(1, _translate("MainWindow", "1", None))
        self.ChoixDuChiffre.setItemText(2, _translate("MainWindow", "2", None))
        self.ChoixDuChiffre.setItemText(3, _translate("MainWindow", "3", None))
        self.ChoixDuChiffre.setItemText(4, _translate("MainWindow", "4", None))
        self.ChoixDuChiffre.setItemText(5, _translate("MainWindow", "5", None))
        self.ChoixDuChiffre.setItemText(6, _translate("MainWindow", "6", None))
        self.ChoixDuChiffre.setItemText(7, _translate("MainWindow", "7", None))
        self.ChoixDuChiffre.setItemText(8, _translate("MainWindow", "8", None))
        self.ChoixDuChiffre.setItemText(9, _translate("MainWindow", "9", None))
        self.choixDuDataset.setItemText(0, _translate("MainWindow", "train_small.csv", None))
        self.choixDuDataset.setItemText(1, _translate("MainWindow", "train_tiny.csv", None))
        self.choixDuDataset.setItemText(2, _translate("MainWindow", "train.csv", None))
        self.start.setText(_translate("MainWindow", "Start !", None))
        self.label.setText(_translate("MainWindow", "Choix du chifre", None))
        self.label_2.setText(_translate("MainWindow", "Choix du dataset", None))
        self.label_3.setText(_translate("MainWindow", "Alpha", None))
        self.label_4.setText(_translate("MainWindow", "Prop dropout", None))
        self.label_5.setText(_translate("MainWindow", "Epsilon", None))
        self.label_6.setText(_translate("MainWindow", "Learning rate", None))
        self.label_7.setText(_translate("MainWindow", "H", None))
        self.label_8.setText(_translate("MainWindow", "Cross-validation", None))
        self.label_9.setText(_translate("MainWindow", "Training", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Neurones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Poids", None))
