# WETS Loukas mat.ULB: 000442311

import sys
from PyQt4 import QtGui
from Gui import *
from mlpFun import *

if __name__ == "__main__":
    
    try:
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        mlp_func=Mlp(ui)
        MainWindow.show()
        sys.exit(app.exec_())
    
    except Exception as error:
        """ THIS EXEPTION CATCH ALL THE ERRORS AND DISPLAY THEM IN A WARNING MESSAGE"""
        error = QtGui.QWidget()
        QtGui.QMessageBox.warning(error, "Error", "{}".format(repr(error)))
        error.show()
